import queue
from queue import PriorityQueue
from math import sqrt

class State(object):
    def __init__(self, value, parent,
                 start = 0, goal = 0):
        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0
        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
        else:
            self.path = [value]
            self.start = start
            self.goal = goal
            
    def GetDist(self):
        pass
    
    def CreateChildren(self):
        pass

class State_Puzzle(State):
    def __init__(self, value, parent, start = 0, goal = 0):
        super(State_Puzzle, self).__init__ (value, parent, start, goal)
        self.dist = self.GetDist()
        
    def GetDist(self):
        if self.value == self.goal:
            return 0
        dist = 0
        size = sqrt(len(self.goal)).real
        for n in range (len(self.goal)):  #9
            piece = self.goal[n]
            goal_x = int(n / size)
            goal_y = n - goal_x * size
            value_x = int(self.value.index(piece) / size)
            value_y = self.value.index(piece) - value_x * size
            
            dist += abs(goal_x - value_x) + abs(goal_y - value_y) #절대값
        
        return dist + len(self.path)
     
    def CreateChildren(self):
        size = int(sqrt(len(self.goal)).real)
        if not self.children:
            i = self.value.index('0')  #리스트에 '0'이 있으면 그 위치값을 반환
            if not int(i % size) == size - 1:
                val = self.value
                val = val[:i] + val[i+1] + val[i] + val[i+2:]  #val[i+1] + val[i] 위치 바꾸는거임
                child = State_Puzzle(val, self)
                self.children.append(child)
            if not int(i % size) == 0:
                val = self.value
                val = val[:i-1] + val[i] + val[i-1] + val[i+1:]
                child = State_Puzzle(val, self)
                self.children.append(child)
            if i < len(self.value) - size:
                val = self.value
                val = val[:i] + val[i+size] + val[i+1:i+size] + val[i] + val[i+size+1:]
                child = State_Puzzle(val, self)
                self.children.append(child)
            if i > size - 1:
                val = self.value
                val = val[:i-size] + val[i] + val[i-size+1:i] + val[i-size] + val[i+1:]
                child = State_Puzzle(val, self)
                self.children.append(child)
                 
class AStar_solver:
    def __init__(self, start, goal):
        self.path = []
        self.visitedQueue = []
        self.priorityQueue = PriorityQueue()
        self.start = start
        self.goal = goal
        
    def Solve(self):
        startState = State_Puzzle(self.start,
                                  0,
                                  self.start,
                                  self.goal)
        count = 0
        self.priorityQueue.put((0, count, startState))
        while(not self.path and self.priorityQueue.qsize()):
            closestChild = self.priorityQueue.get()[2]
            closestChild.CreateChildren()
            self.visitedQueue.append(closestChild.value)
            for child in closestChild.children:
                if child.value not in self.visitedQueue:
                    count += 1
                    if not child.dist:
                        self.path = child.path
                        break
                    self.priorityQueue.put((child.dist, count, child))
        if not self.path:
            print("Goal of " + self.goal + " is not possible")

        return self.path

def display(puzzle,i):

    print(" -----------")
    print("| %c | %c | %c |" % (puzzle[i][0], puzzle[i][1], puzzle[i][2]))
    print(" -----------")
    print("| %c | %c | %c |" % (puzzle[i][3], puzzle[i][4], puzzle[i][5]))
    print(" -----------")
    print("| %c | %c | %c |" % (puzzle[i][6], puzzle[i][7], puzzle[i][8]))
    print(" -----------")


start = "801526347"
goal = "581260347"
print ('starting...')
    
a = AStar_solver(start, goal)
a.Solve()

# print(len(goal))
# print(sqrt(len(goal)))

# print(len(a.path))
# print(a.path[0][0])
# print(a.path[0])
for i in range(len(a.path)):
    print ("%d) " %i)
    display(a.path,i)
