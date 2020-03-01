def star(n):
    if n == 1: return ['*']

    stars = star(n-1)
    start = ['*'+'****'*(n-1)]
    start += ['* '+' '+'    '*(n-2)+' *']
    start += ['* '+ x +' *' for x in stars]
    start += ['* '+' '+'    '*(n-2)+' *']
    start += ['*'+'****'*(n-1)]

    return start

N = int(input())
print(*star(N), sep='\n')