N=int(input())
num = []
for i in range(N):
    num.append(int(input()))

num.sort()
print(*num, sep='\n')