N, X, Y = list(map(int, input().split()))

ans = [0] * (N - 1)
for i in range(1, N):
    for j in range(i + 1, N + 1):
        x = min(j - i, abs(X - i) + 1 + abs(j - Y), abs(Y - i) + 1 + abs(j - X))
        ans[x - 1] += 1
print(*ans, sep="\n")
