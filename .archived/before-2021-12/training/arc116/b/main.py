N = int(input())
A = list(map(int, input().split()))

MOD = 998244353

A.sort()

ans = 0
s = 0
for a in A:
    ans += (s + a) * a
    s = 2 * s + a
    s %= MOD
    ans %= MOD
print(ans % MOD)
