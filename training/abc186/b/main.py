H, W = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(H)]

mi = 101
for r in grid:
    for elem in r:
        mi = min(mi, elem)

ans = 0
for r in grid:
    for elem in r:
        ans += elem - mi

print(ans)
