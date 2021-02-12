from math import log2, ceil
N, K = list(map(int, input().split()))

ans = 0.0
for i in range(1, N + 1):
    tmp = 1.0 / N
    for _ in range(ceil(log2(K / i))):
        tmp /= 2
    ans += tmp
print(ans)
