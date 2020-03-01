class node:
    def __init__(self, data):
        self.path = data
        self.passed = False
        self.link = []

def BFS(V):
    temp = [V]
    result = 0
    V.passed = True
    while len(temp) != 0:
        i = temp.pop(0)
        result += 1
        for j in i.link:
            if j.passed: continue
            j.passed = True
            temp.append(j)

    return result

N = int(input())
seq = [[node(0) for i in range(N+2)]]
for i in range(N):
    seq.append([node(0)] + [node(i) for i in input()] + [node(0)])
seq.append([node(0) for i in range(N+2)])

for i in range(1, N+1):
    for j in range(1, N+1):
        if seq[i][j].path != '1': continue
        if not seq[i - 1][j] in seq[i][j].link and seq[i - 1][j].path == '1':
            seq[i][j].link.append(seq[i - 1][j])
            seq[i - 1][j].link.append(seq[i][j])
        if not seq[i + 1][j] in seq[i][j].link and seq[i + 1][j].path == '1':
            seq[i][j].link.append(seq[i + 1][j])
            seq[i + 1][j].link.append(seq[i][j])
        if not seq[i][j - 1] in seq[i][j].link and seq[i][j - 1].path == '1':
            seq[i][j].link.append(seq[i][j - 1])
            seq[i][j - 1].link.append(seq[i][j])
        if not seq[i][j + 1] in seq[i][j].link and seq[i][j + 1].path == '1':
            seq[i][j].link.append(seq[i][j + 1])
            seq[i][j + 1].link.append(seq[i][j])

result = [0, []]
for i in range(1, N+1):
    for j in range(1, N+1):
        if seq[i][j].path == '1' and not seq[i][j].passed:
            result[0] += 1
            result[1].append(BFS(seq[i][j]))
print(result[0])
print(*sorted(result[1]), sep='\n')