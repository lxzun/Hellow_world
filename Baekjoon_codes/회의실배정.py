import sys
temp = set()
def check(a):
    a = [i for i in range(a[0], a[1])]
    for s in temp:
        if s in a: return False
    return True

N = int(sys.stdin.readline())
seq = [[int(i) for i in sys.stdin.readline().split()] for j in range(N)]

seq = sorted(seq, key=lambda x:x[1])
result = 0
for i in seq:
    if check(i):
        result += 1
        if i[0]!=i[1]:temp.update(set(range(i[0], i[1]+1)))
print(result)