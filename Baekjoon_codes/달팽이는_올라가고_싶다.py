A, B, V = [int(i) for i in input().split()]
i = 1
V -= A
dis = A-B

day = V//dis
left = V%dis

i += day
if left == 0: print(i)
else: print(i+1)
