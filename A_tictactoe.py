# Tic Tac Toe A*
import collections
import copy
import time
from queue import PriorityQueue
from math import sqrt

#플레이어가 o 적은 x

puzzle = ['o', 'x', '8',
        '8', '8', 'x',
        '8', '8', 'o']

goal = ['o', 'x', 'o',
        '8', 'o', 'x',
        'o', '8', 'o']

def display(puzzle):
    print(" -----------")
    print("| %c | %c | %c |" % (puzzle[0], puzzle[1], puzzle[2]))
    print(" -----------")
    print("| %c | %c | %c |" % (puzzle[3], puzzle[4], puzzle[5]))
    print(" -----------")
    print("| %c | %c | %c |" % (puzzle[6], puzzle[7], puzzle[8]))
    print(" -----------")



def check_win(puzzle):
    if ((puzzle[0]==puzzle[1])&(puzzle[0]==puzzle[2])):
        return 1
    elif (puzzle[0]==puzzle[3])&(puzzle[0]==puzzle[6]):
        return 1
    elif (puzzle[0]==puzzle[4])&(puzzle[0]==puzzle[8]):
        return 1
    elif (puzzle[1]==puzzle[4])&(puzzle[1]==puzzle[7]):
        return 1
    elif (puzzle[2]==puzzle[4])&(puzzle[2]==puzzle[6]):
        return 1
    elif (puzzle[2]==puzzle[5])&(puzzle[2]==puzzle[8]):
        return 1
    elif (puzzle[3]==puzzle[4])&(puzzle[3]==puzzle[5]):
        return 1
    elif (puzzle[6]==puzzle[7])&(puzzle[6]==puzzle[8]):
        return 1
    else:
        return 0

def check_null(puzzle):
    checklist=[]
    for i in range(0,len(puzzle)):
        if(puzzle[i]=='8'):
            checklist.append(i)
    return checklist


op = [ 'Up','Middle','Down']
#차례, 플레이어=1  적=0
# 노드 클래스
class Node:
    def __init__(self, state):
        self.state = state

def check_turn(puzzle):
    player_count=0
    enemy_count=0
    for i in range(0,len(puzzle)):
        if(puzzle[i]=='x'):
            player_count=player_count+1
        elif (puzzle[i]=='o'):
            enemy_count=enemy_count+1

    if(player_count==enemy_count):
        return 0
    elif(player_count>enemy_count):
        return 1
    else:
        return 0


def GetDist(puzzle,goal):
    if puzzle == goal:
        return 0
    dist = 0
    size = sqrt(len(goal)).real
    for n in range(len(goal)):  # 9
        if(goal[n]==puzzle[n]):
            dist+=1
        else:
            dist=dist

        # piece = goal[n]
        # goal_x = int(n / size)
        # goal_y = n - goal_x * size
        # value_x = int(puzzle.index(piece) / size)
        # value_y = puzzle.index(piece) - value_x * size

        #dist += abs(goal_x - value_x) + abs(goal_y - value_y)  # 절대값

    return dist


# A*
def A_algorithm(puzzle,goal):
    visit = []
    queue = collections.deque([puzzle])
    checkNull_list = []
    turn = check_turn(puzzle)
    print("시작노드")
    display(puzzle)  # 시작노드
    while queue is not Node:
        print("\n====================")
        print("초기 queue : ", queue)

        xNode = queue.pop()  # 가장 먼저 들어간 노드를 꺼냄

        turn = check_turn(xNode)
        visit.append(xNode)  # 현재 노드를 visit에 추가
        print("visit : ", visit)

        checkNull_list = check_null(xNode)

        if(xNode==goal):
            print("성공")
            display(xNode)
            return 1
        for oper in op:
            # 플레이어턴 o

            if(turn==1):
                newNode = createNode(queue, visit, copy.deepcopy(xNode), checkNull_list, oper,'o') #deep.copy 복사, 주소값 까지
                if(newNode):
                    xNode_dist = GetDist(xNode, goal)
                    newNode_dist = GetDist(newNode, goal)

                    if (xNode_dist >= newNode_dist):
                        queue.append(newNode)
                print("\nnewNode : ", oper, newNode)
            #AI턴 x
            elif(turn==0):
                newNode = createNode(queue, visit, copy.deepcopy(xNode), checkNull_list, oper,'x')  # deep.copy 복사, 주소값 까지
                if (newNode):
                    xNode_dist = GetDist(xNode, goal)
                    newNode_dist = GetDist(newNode, goal)

                    if (xNode_dist >= newNode_dist):
                        queue.append(newNode)
                print("\nnewNode : ", oper, newNode)





# ---------- createNode ----------#
# newNode생성 함수
def createNode(stack, visit, newNode, nullpos, oper,turnvalue):
    for i in range(0,len(nullpos)):
        if oper == 'Up':
            if (nullpos[i] < 3):
                newNode[nullpos[i]]=turnvalue
                if newNode in visit or newNode in stack:
                    return None
                else:
                    return newNode
        elif oper == 'Middle':
            if ((2<nullpos[i])&(nullpos[i]<6)):
                newNode[nullpos[i]]=turnvalue
                if newNode in visit or newNode in stack:
                    return None
                else:
                    return newNode
        elif oper== 'Down':
            if(nullpos[i] > 5):
                newNode[nullpos[i]] = turnvalue
                if newNode in visit or newNode in stack:
                    return None
                else:
                    return newNode




            # ---------- display ----------#



print("\nA*알고리즘\n")
start1 = time.time()  # 시간측정 시작
puzzle = ['o', 'x', 'o',
        '8', '8', 'x',
        '8', '8', 'o']

goal = ['o', 'x', 'o',
        '8', '8', 'x',
        'x', '8', 'o']

A_algorithm(puzzle,goal)
print("A* 소요 시간 : ", time.time() - start1)  # 종료