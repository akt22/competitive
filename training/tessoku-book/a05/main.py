N, K = list(map(int, input().split()))

ans = 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
        tmp = K - (i + j)
        if tmp <= N and tmp > 0:
            ans += 1
print(ans)
