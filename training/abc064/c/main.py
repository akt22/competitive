N = int(input())
A = list(map(int, input().split()))

mi = set()
ma = 0
for a in A:
    if a >= 3200:
        ma += 1
    elif a >= 2800:
        mi.add('r')
    elif a >= 2400:
        mi.add('o')
    elif a >= 2000:
        mi.add('y')
    elif a >= 1600:
        mi.add('bl')
    elif a >= 1200:
        mi.add('c')
    elif a >= 800:
        mi.add('gl')
    elif a >= 400:
        mi.add('br')
    else:
        mi.add('g')
print(max(len(mi), 1), len(mi) + ma)
