import numpy as np

H, W, N = list(map(int, input().split()))

grid = [[0] * (W + 2) for _ in range(H + 2)]
for i in range(N):
    a, b, c, d = list(map(int, input().split()))
    grid[a][b] += 1
    grid[a][d + 1] -= 1
    grid[c + 1][b] -= 1
    grid[c + 1][d + 1] += 1

# acc = [[0] * (W + 1) for _ in range(H + 1)]
# for i in range(1, H + 1):
#     for j in range(1, W + 1):
    # acc[i][j] = acc[i - 1][j] + acc[i][j - 1] - acc[i - 1][j - 1] + grid[i][j]

acc_r = np.array(grid).cumsum(axis=0)
acc = acc_r.cumsum(axis=1)

for row in acc[1:-1]:
    print(*row[1:-1])
