from cmath import inf
import math

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(N)]

INF = 1 << 60


def d(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


ans = 0.
for i, (x1, y1) in enumerate(XY):
    nearest = INF
    for a in A:
        x2, y2 = XY[a - 1]
        nearest = min(nearest, d(x1, y1, x2, y2))
    ans = max(ans, nearest)
print(ans)
