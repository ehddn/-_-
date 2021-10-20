def splitDataSet(dataSet, axis, value):
    retDataSet = []
    #print(dataSet)
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:1])
            retDataSet.append(reducedFeatVec)

    print(retDataSet)
    return retDataSet

dataSet = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
labels = ['no surfacing', 'flippers']

print(dataSet[0][0:1])
# retDataSet = []
#     #print(dataSet)
# for featVec in dataSet:
#     if featVec[0] == 0:
#         reducedFeatVec = featVec[:1]
#         reducedFeatVec.extend(featVec[0 + 1:1])
#         retDataSet.append(reducedFeatVec)
# print(retDataSet)
# subDataSet = splitDataSet(dataSet, 0, 0)