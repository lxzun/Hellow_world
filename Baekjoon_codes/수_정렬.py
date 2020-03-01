def counting_sort(num, M):
    result = [-1] * len(num)
    C = [0] * (M + 1)

    for i in num:
        C[i] += 1

    for i in range(M):
        C[i + 1] += C[i]

    for j in reversed(range(len(num))):
        result[C[num[j]] - 1] = num[j]
        C[num[j]] -= 1
    return result

N = int(input())
num = []
for i in range(N):
    num.append(int(input()))
M = max(num)
print(*counting_sort(num, M))