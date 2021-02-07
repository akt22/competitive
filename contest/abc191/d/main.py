from math import floor, ceil
from decimal import Decimal
X, Y, R = map(Decimal, input().split())


def cf(x, r):
    return ceil(x - r), floor(x + r)


ans = 0
start, end = cf(X, R)
for i in range(start, end + 1):
    p = Decimal(R**2 - (X - i)**2).sqrt()
    bottom, top = cf(Y, p)
    ans += top - bottom + 1
print(ans)
