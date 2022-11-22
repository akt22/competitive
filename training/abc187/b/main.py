N = int(input())
points = [list(map(float, input().split())) for _ in range(N)]

ans = 0
for idx, (x1, y1) in enumerate(points):
    for x2, y2 in points[idx + 1:]:
        g = (y2 - y1) / (x2 - x1)
        if -1 <= g <= 1:
            ans += 1
print(ans)
