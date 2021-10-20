from collections import deque
from random import randint

import sys

start = [2,8,3,1,6,4,7,0,5]
goal = [2,8,3,1,0,4,7,6,5]


def up(X):
    index = 0
    for i in range(len(X)):
        if X[i] == 0:
            index = i
    #맨 윗줄이라면 그대로
    if index == 0 or index == 1 or index == 2:
        return X
    #아니라면 한칸 위로
    else:
        X[index] = X[index - 3]
        X[index - 3] = 0
        return X


def down(X):
    index = 0
    for i in range(len(X)):
        if X[i] == 0:
            index = i
    #맨 아랫줄이라면 그대로
    if index == 6 or index == 7 or index == 8:
        return X
    #아니라면 한칸 아래로
    else:
        X[index] = X[index + 3]
        X[index + 3] = 0
        return X


def right(X):
    index = 0
    for i in range(len(X)):
        if X[i] == 0:
            index = i
    #맨 오른쪽 라인이라면 그대로
    if index == 2 or index == 5 or index == 8:
        return X
    #아니라면 한칸 오른쪽으로
    else:
        X[index] = X[index + 1]
        X[index + 1] = 0
        return X


def left(X):
    index = 0
    for i in range(len(X)):
        if X[i] == 0:
            index = i
    #맨 왼쪽 라인이라면 그대로
    if index == 0 or index == 3 or index == 6:
        return X
    #아니라면 한칸 왼쪽으로
    else:
        X[index] = X[index - 1]
        X[index - 1] = 0
        return X


def depth_first_search():
    print(" 깊이 우선 탐색 ")
    open = [start]  # 시작노드
    closed = []

    print("시작노드:", open)
    count = 1
    while open != []:
        X = open[0]
        print("현재노드:", count, ": ")
        print("현재 open LIST ", open)
        print("-------------")
        print("|", X[0], "|", X[1], "|", X[2], "|")
        print("-------------")
        print("|", X[3], "|", X[4], "|", X[5], "|")
        print("-------------")
        print("|", X[6], "|", X[7], "|", X[8], "|")
        print("-------------\n")

        count = count + 1

        if X == goal:
            print("Success")
            return True
        else:
            # X의 자식 노드를 생성한다
            child = []
            tmp = (tuple(X))

            child.append(down(list(tmp)))

            child.append(right(list(tmp)))  # 여백이 오른쪽으로 이동한거

            child.append(up(list(tmp)))  # 여백이 가운데로 이동한거

            child.append(left(list(tmp)))  # 여백이 왼쪽으로 이동한거

        #탐색을 끝낸 리스트는 closed 리스트에 할당
        closed.append(X)
        #open리스트에서 x를 제거  open리스트를 큐처럼 사용
        open.remove(X)

        for i in range(len(child)):
            if child[i] not in open and child[i] not in closed:
                open.insert(0, child[i])

    print("Fail")
    return False


def breadth_first_search():
    print(" ======== 너비 우선 탐색 =========")
    open = [start]
    closed = []

    print("시작노드:", open)
    count = 1
    while open != []:
        X = open[0]
        print("현재노드:", count, ": ")
        print("현재 open LIST ", open)
        print("-------------")
        print("|", X[0], "|", X[1], "|", X[2], "|")
        print("-------------")
        print("|", X[3], "|", X[4], "|", X[5], "|")
        print("-------------")
        print("|", X[6], "|", X[7], "|", X[8], "|")
        print("-------------\n")
        count = count + 1

        if X == goal:
            print("Success")
            return True
        else:
            child = []
            tmp = (tuple(X))

            child.append(down(list(tmp)))

            child.append(right(list(tmp)))

            child.append(up(list(tmp)))

            child.append(left(list(tmp)))

        closed.append(X)
        open.remove(X)

        for i in range(len(child)):
            if child[i] not in open and child[i] not in closed:
                open.append(child[i])

    print("Fail")
    return False


#depth_first_search()
breadth_first_search()