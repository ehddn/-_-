# Tic Tac Toe bfs(너비 우선 탐색), dfs(깊이 우선 탐색)
import collections
import copy
import time

#플레이어가 o 적은 x

puzzle = ['o', 'x', '8',
        'o', '8', 'x',
        'x', '8', 'o']

goal = [1, 2, 3,
          4, 5, 6,
          0, 7, 8]

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


# ---------- DFS ----------#
# 깊이 우선 탐색
def depth_first_search(puzzle):
    visit = []  # closed
    stack = collections.deque([puzzle])  # open #양방향 형식 디큐 사용
    checkNull_list=[]
    turn=check_turn(puzzle)
    count=0
    print("시작노드")
    display(puzzle)  # 시작노드
    while stack is not Node:
        print("\n====================")
        print("stack : ", stack)
        xNode = stack.pop()  # 가장 마지막 노드를 꺼냄
        print("xNode : ", xNode, "\n")
        #display(xNode)  # 현재 상태 노드 출력
        turn=check_turn(xNode)
        print("차례: ",turn)

        visit.append(xNode)  # 현재 노드를 visit에 추가
        print("visit : ", visit)
        #display(xNode)
        checkNull_list=check_null(xNode)
        check = check_win(xNode)

        if check == 1:
            #display(xNode)  #그림상 쉽게 보이기 위해
            display(xNode)
            return print("\nSUCESS!")
        else:
            for oper in op:
                # 새로운 노드 생성
                if(turn==1):
                    newNode = createNode(stack, visit, copy.deepcopy(xNode), checkNull_list, oper,'o') #deep.copy 복사, 주소값 까지
                    print("\nnewNode : ", oper, newNode)
                elif(turn==0):
                    newNode = createNode(stack, visit, copy.deepcopy(xNode), checkNull_list, oper,'x')  # deep.copy 복사, 주소값 까지
                    print("\nnewNode : ", oper, newNode)

                if newNode is not None:  # 새로운 노드가 있다면
                    stack.append(newNode)  # stack(opnen)에 추가
                    # print("stack : ", stack)
                    print()





# ---------- BFS ----------#
# 너비 우선 탐색
def breadth_first_search(puzzle):
    visit = []
    queue = collections.deque([puzzle])
    checkNull_list = []
    turn = check_turn(puzzle)
    print("시작노드")
    display(puzzle)  # 시작노드
    while queue is not Node:
        print("\n====================")
        print("초기 queue : ", queue)

        xNode = queue.popleft()  # 가장 먼저 들어간 노드를 꺼냄

        print("xNode : ", xNode, "\n")
        turn = check_turn(xNode)
        print("차례: ", turn)

        visit.append(xNode)  # 현재 노드를 visit에 추가
        print("visit : ", visit)
        #display(xNode)
        checkNull_list = check_null(xNode)

        for oper in op:
            # 플레이어턴 o
            check = check_win(xNode)
            if check == 1:
                display(xNode)
                return print("\nSUCESS!")
            else:
                if(turn==1):
                    newNode = createNode(queue, visit, copy.deepcopy(xNode), checkNull_list, oper,'o') #deep.copy 복사, 주소값 까지
                    print("\nnewNode : ", oper, newNode)
                #AI턴 x
                elif(turn==0):
                    newNode = createNode(queue, visit, copy.deepcopy(xNode), checkNull_list, oper,'x')  # deep.copy 복사, 주소값 까지
                    print("\nnewNode : ", oper, newNode)
            if newNode is not None:  # 새로운 노드가 있다면
                queue.append(newNode)  # stack(opnen)에 추가
                # print("stack : ", stack)
                print()






# ---------- checkPosition ----------#
# 0의 위치를 체크하는 함수
def checkPosition(xNode):
    i = xNode.index(0)  # 0의 인덱스를 반
    return i


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



# print("\n*깊이 우선 탐색*\n")
# start1 = time.time()  # 시간측정 시작
# depth_first_search(puzzle)
# print("DFS 소요 시간 : ", time.time() - start1)  # 종료

# ---------- main ----------#
# node = Node(puzzle)
#
print("\n*깊이 우선 탐색*\n")
start1 = time.time()  # 시간측정 시작
depth_first_search(puzzle)
print("DFS 소요 시간 : ", time.time() - start1)  # 종료

# start2 = time.time()  # 시간측정 시작
# print("\n*너비 우선 탐색*\n")
# breadth_first_search(puzzle)
# print("BFS소요 시간 : ", time.time() - start2)  # 종료