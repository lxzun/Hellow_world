seq = input().split('-')
seq = [sum(map(int, i.split('+'))) for i in seq]
print(seq[0]-sum(seq[1:]))