H, W = list(map(int, input().split()))
N = int(input())
A = list(map(int, input().split()))

colors = []
for idx, a in enumerate(A):
    colors.extend([idx + 1] * a)

grids = [[0] * W for _ in range(H)]

idx = 0
for y in range(H):
    w = range(W) if y % 2 == 0 else range(W - 1, -1, -1)
    for x in w:
        grids[y][x] = colors[idx]
        idx += 1
for row in grids:
    print(*row)
