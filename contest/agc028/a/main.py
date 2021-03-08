from math import gcd

N, M = list(map(int, input().split()))
S = input()
T = input()

d = {}

L = N * M // gcd(N, M)

for idx, s in enumerate(S):
    i = (L // N) * idx + 1
    d[i] = s

for idx, t in enumerate(T):
    i = (L // M) * idx + 1
    if i in d and d[i] != t:
        print(-1)
        exit()
print(L)
