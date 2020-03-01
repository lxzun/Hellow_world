import copy
import sys
sys.setrecursionlimit(10**6)

def DFS(V):
    V[1] = True
    temp = [V[0]]
    if len(V[2]) != 0:
        V[2] = sorted(V[2], key=lambda x: x[0])
        for i in V[2]:
            if i[1]: continue
            temp.extend(DFS(i))
    return temp

def BFS(V):
    temp = [V]
    result = [V[0]]
    V[1] = True
    while len(temp) != 0:
        i = temp.pop(0)
        if len(i[2]) != 0:
            i[2] = sorted(i[2], key=lambda x: x[0])
            for j in i[2]:
                if j[1]: continue
                j[1] = True
                result.append(j[0])
                temp.append(j)
    return result

N, M, V = [int(i) for i in input().split()]
N = [[i+1, False, []] for i in range(N)]
for i in range(M):
    j, k = [int(i)-1 for i in input().split()]
    N[j][2].append(N[k])
    N[k][2].append(N[j])

A = copy.deepcopy(N)

print(DFS(A[V-1]))
print(BFS(N[V-1]))