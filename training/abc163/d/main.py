N, K = list(map(int, input().split()))

MOD = 10**9 + 7
ans = 0
for i in range(K, N + 1):
    start = i * (i - 1) // 2
    end = i * (N + (N - i + 1)) // 2
    ans += end - start + 1
    ans %= MOD
print(ans + 1)
