N, K = map(int, input().split())
candles = list(map(int, input().split()))

ans = 10**9
for i in range(N - K + 1):
    l, r = candles[i], candles[i + K - 1]
    lr = abs(l) + abs(r - l)
    rl = abs(r) + abs(l - r)
    ans = min(ans, lr, rl)

print(ans)
