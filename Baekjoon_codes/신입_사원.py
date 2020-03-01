import sys
input_func = sys.stdin.readline

def func(seq):
    seq, M = seq[0], seq[1]
    seq.sort(key=lambda x:x[0])
    a = seq[0][1]
    res = [seq[0]]
    for i in range(1, M):
        if seq[i][1] < a:
            res.append(seq[i])
            a = seq[i][1]

    return len(res)

N = int(input())
main_seq = []
for _ in range(N):
    seq = []
    M = int(input())
    for _ in range(M):
        a, b = map(int, input_func().strip().split())
        seq.append((a, b))
    main_seq.append([seq, M])

for i in main_seq:
    print(func(i))