N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]


def d(x1, y1, x2, y2):
    return abs(x1 - x2)**2 + abs(y1 - y2)**2


ans = 0.
for i, (x1, y1) in enumerate(points[:-1]):
    for x2, y2 in points[i + 1:]:
        ans = max(ans, d(x1, y1, x2, y2))
print(ans**0.5)
