def func(confetti):
    M = len(confetti)
    zero = 0
    one = 0
    for i in range(M):
        if 0 in confetti[i] and not 1 in confetti[i]:
            zero += 1
        elif 1 in confetti[i] and not 0 in confetti[i]:
            one += 1
    if zero == M: return 1, 0
    if one == M: return 0, 1

    w, b = 0, 0
    nexts = int(M/2)
    w_, b_ = func([i[:nexts] for i in confetti[:nexts]])
    w += w_;
    b += b_
    w_, b_ = func([i[nexts:] for i in confetti[:nexts]])
    w += w_;
    b += b_
    w_, b_ = func([i[:nexts] for i in confetti[nexts:]])
    w += w_;
    b += b_
    w_, b_ = func([i[nexts:] for i in confetti[nexts:]])
    w += w_;
    b += b_
    return w, b


N = int(input())

confetti = [[int(i) for i in input().split()] for _ in range(N)]
print(*func(confetti), sep='\n')