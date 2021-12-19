H, W = list(map(int, input().split()))

matrix = [list(map(int, input().split())) for _ in range(H)]

column = [0] * W
row = [0] * H
for i in range(H):
    for j in range(W):
        column[j] += matrix[i][j]
        row[i] += matrix[i][j]

for i in range(H):
    r = []
    for j in range(W):
        r.append(column[j] + row[i] - matrix[i][j])
    print(*r)
