N = input()
time = [int(i) for i in input().split()]
time.sort(reverse=True)
a = 0
for i, x in enumerate(time):
    a += x*(i+1)
print(a)