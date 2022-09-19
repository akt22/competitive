H, W = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(H)]

Q = int(input())
questions = [list(map(int, input().split())) for _ in range(Q)]

acc = [[0] * (W + 1) for _ in range(H + 1)]
for i in range(H):
    for j in range(W):
        acc[i + 1][j + 1] = acc[i][j + 1] + acc[i + 1][j] - acc[i][j] + grid[i][j]

for a, b, c, d in questions:
    print(acc[c][d] - acc[a - 1][d] - acc[c][b - 1] + acc[a - 1][b - 1])
