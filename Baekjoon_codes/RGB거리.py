N = int(input())
cost = [[int(i) for i in input().split()] for j in range(N)]

for i in range(1, N):
    for j in range(3):
        cost[i][j] = min(cost[i-1][j-1], cost[i-1][j-2]) + cost[i][j]


print(min(cost[N-1]))