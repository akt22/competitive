from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))

MOD = 10**9 + 7
sums = list(accumulate(A, lambda x, y: (x + y) % MOD))

ans = 0
for idx, a in enumerate(A):
    ans += a * (sums[-1] - sums[idx])
    ans %= MOD
print(ans)
