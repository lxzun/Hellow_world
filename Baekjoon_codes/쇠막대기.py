seq = input().split('()')
state = 0
count = 0
result = 0
for i in seq:
    result += state
    state += i.count('(')
    close = i.count(')')
    result += close
    state -= close

print(result)