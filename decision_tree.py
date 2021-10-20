from math import log
import operator



def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    return dataSet, labels


def calcShannonEnt(dataSet):
    numEntries = len(dataSet)

    # dataset들의 label과 그 개수가 들어갈 딕셔너리.
    # {'yes' :  13 , 'no' : 14} 같은 형식으로 사용될 것이다.
    labelCounts = {}

    # dataSet(정보들의 2차원 set)에서 featVec(정보 set 1개)를 추출
    # 정보 set의 마지막 element인 label을 추출해 labelCounts에 추가
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys(): labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1

    shannonEnt = 0.0
    # levelConts의 key, 즉 모든 label에 대해 확률을 계산 후 더한다.
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt

def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1      # 데이터를 구성하고 있는 set의 마지막 elements는 feature가 아닌 label에 대한 정보이므로 1을 뺍니다.
    baseEntropy = calcShannonEnt(dataSet)     # dataSet를 나누기 전의 셰넌 엔트로피를 계산합니다.

    bestInfoGain = 0.0; bestFeature = -1

    # 각 속성에 따른 분류에 대해 계산해야 하므로, 속성의 개수번만큼 반복합니다.
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]     # 각 데이터의 i번째 element들으로 List를 만듭니다.
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


def majorityCnt(classList):
    classCount = {}
    # 하나씩 꺼내서 계수
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1

    # 내림차순으로 정렬, 가장 앞에 있는(가장 투표 수가 높은) class 선정
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]

    # 재귀 탈출조건
    if classList.count(classList[0]) == len(classList):
        return classList[0] # 조건 1. 분할된 dataSet (== classList)의 모든 label이 같을 것
    if len(dataSet[0]) == 1:
        return majorityCnt(classList) # 조건 2. 모든 속성을 분할에 사용하여 더이상 분할할 수 없는 경우

    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}} # 트리는 딕셔너리 방식으로 만들어짐.
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:] # 파이썬에서는 깊은 복사가 일어나므로, 1개의 label 저장소를 더 만들어 주어야 함
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),subLabels)
    return myTree

def getNumLeafs(myTree):
    numLeafs = 0
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if isinstance(secondDict[key], dict):
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs


def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if isinstance(secondDict[key], dict):
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth > maxDepth:
            maxDepth = thisDepth
    return maxDepth


import matplotlib.pyplot as plt
decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")

def plotNode(nodeTxt, centerPt, parentPt, nodeType, ax):
    ax.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction',
                xytext=centerPt, textcoords='axes fraction',
                va="center", ha="center", bbox=nodeType,
                arrowprops=arrow_args)


def plotMidText(cntrPt, parentPt, txtString, ax):
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    ax.text(xMid, yMid, txtString, va="center", ha="center",
            rotation=30)


def plotTree(myTree, parentPt, nodeTxt, totalW, totalD, xyOff, ax):
    numLeafs = getNumLeafs(myTree)
    firstStr = list(myTree.keys())[0]
    cntrPt = (xyOff[0] + (1 + numLeafs) / (2 * totalW), xyOff[1])
    plotMidText(cntrPt, parentPt, nodeTxt, ax)
    plotNode(firstStr, cntrPt, parentPt, decisionNode, ax)
    secondDict = myTree[firstStr]
    xyOff[1] -= 1 / totalD
    for key in sorted(secondDict.keys()):
        if isinstance(secondDict[key], dict):
            plotTree(secondDict[key], cntrPt, str(key),
                     totalW, totalD, xyOff, ax)
        else:
            xyOff[0] += 1.0 / totalW
            plotNode(secondDict[key], (xyOff[0], xyOff[1]), cntrPt,
                     leafNode, ax)
            plotMidText((xyOff[0], xyOff[1]), cntrPt, str(key), ax)
    xyOff[1] += 1 / totalD


def createPlot(inTree, figsize):
    fig, ax = plt.subplots(subplot_kw={'xticks':[], 'yticks':[],
                                       'frameon':False},
                           figsize=figsize)
    totalW = getNumLeafs(inTree)
    totalD = getTreeDepth(inTree)
    xyOff = [-0.5 / totalW, 1]
    plotTree(inTree, (0.5, 1.0), '', totalW, totalD, xyOff, ax)
    plt.show()

def classify(inputTree,featLabels,testVec):
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    key = testVec[featIndex]
    valueOfFeat = secondDict[key]
    if isinstance(valueOfFeat, dict):
        classLabel = classify(valueOfFeat, featLabels, testVec)
    else: classLabel = valueOfFeat
    return classLabel


def storeTree(inputTree, filename):
    import pickle
    fw = open(filename, "wb")
    pickle.dump(inputTree, fw)
    fw.close()


def grabTree(filename):
    import pickle
    fr = open(filename, "rb")
    return pickle.load(fr)

fr = open('word_training.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels = ["Age",'Gender','Keyword','feeling','word']
lensesTree = createTree(lenses, lensesLabels)
print(lensesTree)

createPlot(lensesTree, (20, 20))