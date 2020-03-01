def star(n):
    if n == 1: return ['*']

    if n % 2 == 0:
        stars = star(n - 1)
        start = [stars[-1] * 2 + '***']

        for i, x in enumerate(stars):
            s = ' '*(i+1)
            s += '*'

            temp = int(len(x)-1-(2*i))
            s += ' '*(temp) + x
            s += ' '*(temp*2)
            s += '*'

            start.append(s)

        for i, x in enumerate(stars):
            s = ' '*(len(x)+1)
            s += '*'

            temp = int(len(stars[-1])-2-(2*i))
            s += ' '*temp
            if x != stars[-1]: s += '*'

            start.append(s)

        return start

    else:
        stars = star(n - 1)
        start = []
        k = 0

        for i, x in enumerate(stars):
            s = ' '*(len(x)+1)
            s += '*'
            if i != 0:
                s += ' '*((i-1)*2+1)
                s += '*'
            start.append(s)
            k = i +1

        for i, x in enumerate(stars):
            s = ' '*(k - i)
            s += '*'

            temp = int(len(stars[0])-(len(stars[0])-2*i))
            s += ' '*(temp//2) + x
            s += ' '*temp
            s += '*'

            start.append(s)

        start += [stars[0] * 2 + '***']
        return start

N = int(input())
print(*star(N), sep='\n')