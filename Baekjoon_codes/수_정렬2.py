def heapsort(un, idx, size):
    M = idx
    l_idx = 2*idx + 1
    r_idx = 2*idx + 2
    if l_idx < size and un[l_idx] > un[M]: M = l_idx
    if r_idx < size and un[r_idx] > un[M]: M = r_idx
    if M != idx:
        un[M], un[idx] = un[idx], un[M]
        heapsort(un, M, size)

N = int(input())
num = [int(input())]
for i in range(N):
    num.append(i)
heapsort(num, 0, len(num))
print(*num, sep='\n')