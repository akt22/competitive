N, K = list(map(int, input().split()))

ans = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        v = K - (i + j)
        if 0 < v <= N:
            ans += 1
print(ans)
