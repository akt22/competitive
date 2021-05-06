H, W, K, V = map(int, input().split())

lands = [list(map(int, input().split())) for _ in range(H)]

s = [[0] * (W + 1) for _ in range(H + 1)]


for i in range(H):
    for j in range(W):
        s[i + 1][j + 1] = s[i][j + 1] + s[i + 1][j] - s[i][j] + lands[i][j]

ans = 0
for i in range(1, H + 1):
    for j in range(1, W + 1):
        for k in range(1, i + 1):
            for l in range(1, j + 1):
                if (s[i][j] + s[i - k][j - l] - s[i - k][j] - s[i][j - l] + (k * l * K) <= V):
                    ans = max(ans, k * l)

print(ans)
