xy = set(map(int, input().split()))
hands = set([0, 1, 2])

if len(xy) == 1:
    print(list(xy)[0])
else:
    print(list(hands - xy)[0])
