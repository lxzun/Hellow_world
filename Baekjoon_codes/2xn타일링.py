def func(n):
    seq = [1, 2]
    if len(seq) < n:
        for i in range(n-2):
            seq.append(seq[-1]+seq[-2])
    return seq[n-1]

n = int(input())
print(func(n))