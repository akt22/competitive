A, B = list(map(int, input().split()))

a = set()
if A == 0:
    pass
elif A == 1:
    a.add(1)
elif A == 2:
    a.add(2)
elif A == 3:
    a.add(1)
    a.add(2)
elif A == 4:
    a.add(4)
elif A == 5:
    a.add(1)
    a.add(4)
elif A == 6:
    a.add(2)
    a.add(4)
else:
    a.add(1)
    a.add(2)
    a.add(4)

b = set()
if B == 0:
    pass
elif B == 1:
    b.add(1)
elif B == 2:
    b.add(2)
elif B == 3:
    b.add(1)
    b.add(2)
elif B == 4:
    b.add(4)
elif B == 5:
    b.add(1)
    b.add(4)
elif B == 6:
    b.add(2)
    b.add(4)
else:
    b.add(1)
    b.add(2)
    b.add(4)


print(sum(list(a | b)))
