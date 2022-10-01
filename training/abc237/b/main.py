H, W = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(H)]

for y in range(W):
    row = []
    for x in range(H):
        row.append(matrix[x][y])
    print(*row)
