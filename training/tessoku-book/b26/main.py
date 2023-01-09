from math import sqrt

N = int(input())

deleted = [False] * (N + 1)

for i in range(2, int(sqrt(N)) + 1):
    if deleted[i]:
        continue
    for j in range(i * 2, N + 1, i):
        deleted[j] = True

for i, v in enumerate(deleted):
    if i > 1 and not v:
        print(i)
