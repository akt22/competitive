import math

A, B = list(map(int, input().split()))

base = B - A

for i in range(base, 0, -1):
    c = math.ceil(A / i)
    f = math.floor(B / i)

    if c != f:
        print(i)
        exit()
