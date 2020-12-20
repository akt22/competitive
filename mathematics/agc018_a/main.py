from math import gcd

N, K = map(int, input().split())
A = list(map(int, input().split()))

M = max(A)

if K > M:
    print("IMPOSSIBLE")
    exit()

g = 0
for a in A:
    g = gcd(g, a)

if K % g == 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
