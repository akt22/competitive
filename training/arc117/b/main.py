N = int(input())
A = list(map(int, input().split()))


MOD = 10**9 + 7

A.sort()
ans = 1
prev = 0
for a in A:
    ans *= a - prev + 1
    ans %= MOD
    prev = a
print(ans)
