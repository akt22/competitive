N = int(input())
X = list(map(int, input().split()))

Xs = sorted(X)

h = N // 2
for x in X:
    if x < Xs[h]:
        print(Xs[h])
    else:
        print(Xs[h - 1])
