import math

T = int(input())
L, X, Y = list(map(int, input().split()))
Q = int(input())
E = [int(input()) for _ in range(Q)]


def distance(x, y, z):
    _x = x - X
    _y = y - Y
    _z = z
    return math.sqrt(_x**2 + _y**2 + _z**2)


def degree(a, b):
    return math.degrees(math.asin(a / b))


for e in E:
    th = e / T
    y = (-L / 2) * math.sin(2 * th * math.pi)
    z = (L / 2) - (L / 2) * math.cos(2 * th * math.pi)
    d = distance(0, y, z)
    print(degree(z, d))
