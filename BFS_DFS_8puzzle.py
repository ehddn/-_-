# 8-puzzle bfs(너비 우선 탐색), dfs(깊이 우선 탐색)
import collections
import copy
import time

# #BFS용 예시
# goal = [1, 2, 3,
#         4, 5, 6,
#         7, 8, 0]
#
# puzzle = [1, 2, 3,
#           4, 5, 6,
#           0, 7, 8]


#DFS용 예시
# puzzle = [3, 1, 2,
#           6, 4, 5,
#           0, 7, 8]
#
# goal = [0, 1, 2,
#         3, 4, 5,
#         6, 7, 8]

puzzle = [3, 1, 0,
          6, 4, 5,
          2, 7, 8]

goal = [6, 3, 1,
        4, 5, 8,
        0, 2, 7]

op = ['UP', 'DOWN', 'RIGHT', 'LEFT']


# 노드 클래스
class Node:
    def __init__(self, state):
        self.state = state


# ---------- DFS ----------#
# 깊이 우선 탐색
def depth_first_search(puzzle):
    visit = []  # 방문한 노드 목록
    stack = collections.deque([puzzle])  # 퍼즐 스택
    print("Goal : ", goal)
    while stack is not Node:
        print("====================")
        print("stack : ", stack)

        xNode = stack.pop()  # 가장 마지막 노드를 꺼냄

        print("xNode : ", xNode, "\n")
        display(xNode)  # 현재 상태 노드 출력

        if xNode == goal:  # 현재 상태 노드가 목표상태와 같다면 성공
            return print("\nSUCESS!")




        else:
            visit.append(xNode)  # 현재 노드를 visit에 추가
            print("visit : ", visit)

            # 0 위치를 확인한 후 0 위치 인덱스 반환
            index = checkPosition(xNode)
            print("'0'index :", index)

            # 모든 연산자에 대해 조회
            for oper in op:
                # 새로운 노드 생성
                newNode = createNode(stack, visit, copy.deepcopy(xNode), index, oper) #deep.copy 복사, 주소값 까지
                print("\nnewNode : ", oper, newNode)

                if newNode is not None:  # 새로운 노드가 있다면
                    stack.append(newNode)  # stack(opnen)에 추가
                    # print("stack : ", stack)
                    print()


# ---------- BFS ----------#
# 너비 우선 탐색
def breadth_first_search(puzzle):
    visit = []  # 방문한 노드 목록
    queue = collections.deque([puzzle])  # 퍼즐 큐
    print("Goal : ", goal)
    while queue is not Node:
        print("\n====================")
        print("초기 queue : ", queue)

        xNode = queue.popleft()  # 가장 먼저 들어간 노드를 꺼냄

        print("xNode : ", xNode, "\n")
        display(xNode)  # 현재 상태 노드 출력

        if xNode == goal:
            return print("\nSUCESS!")

        else:
            visit.append(xNode)
            print("visit : ", visit)

            index = checkPosition(xNode)
            print("'0'index :", index)

            for oper in op:
                newNode = createNode(queue, visit, copy.deepcopy(xNode), index, oper)
                print("\nnewNode : ", oper, newNode)

                if newNode is not None:
                    queue.append(newNode)
                    print(" : ", queue)
                    print()


# ---------- checkPosition ----------#
# 0의 위치를 체크하는 함수
def checkPosition(xNode):
    i = xNode.index(0)  # 0의 인덱스를 반
    return i


# ---------- createNode ----------#
# newNode생성 함수
def createNode(stack, visit, newNode, i, oper):
    if oper == 'UP':
        if (i >= 3):
            newNode[i] = newNode[i - 3]
            newNode[i - 3] = 0

            if newNode in visit or newNode in stack:
                return None
            else:
                return newNode

    if oper == 'DOWN':
        if (i < 6):
            newNode[i] = newNode[i + 3]
            newNode[i + 3] = 0

            if newNode in visit or newNode in stack:
                return None
            else:
                return newNode

    if oper == 'RIGHT':
        if ((i % 3) < 2):
            newNode[i] = newNode[i + 1]
            newNode[i + 1] = 0

            if newNode in visit or newNode in stack:
                return None
            else:
                return newNode
    if oper == 'LEFT':
        if ((i % 3) > 0):
            newNode[i] = newNode[i - 1]
            newNode[i - 1] = 0

            if newNode in visit or newNode in stack:
                return None
            else:
                return newNode

            # ---------- display ----------#


def display(puzzle):
    print(" -----------")
    print("| %d | %d | %d |" % (puzzle[0], puzzle[1], puzzle[2]))
    print(" -----------")
    print("| %d | %d | %d |" % (puzzle[3], puzzle[4], puzzle[5]))
    print(" -----------")
    print("| %d | %d | %d |" % (puzzle[6], puzzle[7], puzzle[8]))
    print(" -----------")


# ---------- main ----------#
node = Node(puzzle)

# print("\n*깊이 우선 탐색*\n")
# start1 = time.time()  # 시간측정 시작
# depth_first_search(puzzle)
# print("DFS 소요 시간 : ", time.time() - start1)  # 종료

start2 = time.time()  # 시간측정 시작
print("\n*너비 우선 탐색*\n")
breadth_first_search(puzzle)
print("BFS소요 시간 : ", time.time() - start2)  # 종료