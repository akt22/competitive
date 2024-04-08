from math import sqrt

Q = int(input())
X = [int(input()) for _ in range(Q)]

N = 300000
cache = [False] * 300001

for i in range(2, int(sqrt(N)) + 1):
    if cache[i]:
        continue
    for j in range(i * 2, N + 1, i):
        cache[j] = True

for x in X:
    print("No" if cache[x] else "Yes")
