import numpy as np

N, M = list(map(int, input().split()))
L, R = [], []

for _ in range(M):
    l, r = list(map(int, input().split()))
    L.append(l)
    R.append(r)

l, r = max(L), min(R)

if l > r:
    print(0)
else:
    print(r - l + 1)
