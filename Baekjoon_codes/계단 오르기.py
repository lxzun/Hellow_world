N = int(input())
stair = [[int(input())]*2 for i in range(N)]
stair[1][1] += stair[0][1]
for i in range(2,N):
    stair[i][0] += max(stair[i-2])
    stair[i][1] += stair[i-1][0]
print(max(stair[-1]))