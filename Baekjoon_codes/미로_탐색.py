import numpy as np
class node():
    def __init__(self, passing, goal):
        self.goal = goal
        self.passing = bool(passing)
        self.passed = True
        self.link = []

    def connect(self, node):
        self.link.append(node)

    def passnode(self):
        self.passed = False

    def checkpassed(self):
        return self.passed

    def __iter__(self):
        self.id = 0
        return self

    def __next__(self):
        if self.id >= len(self.link):
            raise StopIteration
        n = self.link[self.id]
        self.id += 1
        return n

class maze():
    def __init__(self, node, mazelist):
        node.passnode()
        self.n = 1
        self.qu = [node]
        self.make(mazelist)

    def make(self, mazelist):
        maze = np.array(mazelist)
        N, M = maze.shape
        for i in range(N):
            for j in range(M):
                if maze[i, j].passing == False: continue
                if i - 1 >= 0: maze[i, j].connect(maze[i - 1, j])
                if j - 1 >= 0: maze[i, j].connect(maze[i, j - 1])
                if i + 1 < N: maze[i, j].connect(maze[i + 1, j])
                if j + 1 < M: maze[i, j].connect(maze[i, j + 1])

    def next(self):
        temp = []
        self.n += 1
        for k in self.qu:
            for i in k:
                if i.goal: return self.n
                if i.checkpassed():
                    i.passnode()
                    temp.append(i)
        self.qu = temp
        return None

N, M = [int(i) for i in input().split()]
mazelist = []

for i in range(N):
    temp = [node(int(x), [i, j]==[N-1, M-1]) for j, x in enumerate(input())]
    mazelist.append(temp)

maze = maze(mazelist[0][0], mazelist)
while True:
    n = maze.next()
    if n != None:break

print(n)