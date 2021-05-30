from math import factorial

N, M = list(map(int, input().split()))

if abs(N - M) > 1:
    print(0)
    exit()

MOD = 10**9 + 7
d = factorial(N) % MOD
m = factorial(M) % MOD

if (N + M) % 2 == 0:
    print(d * m * 2 % MOD)
else:
    print(d * m % MOD)
