from itertools import accumulate

N, X = map(int, input().split())

a = []
for _ in range(N):
    v, p = map(int, input().split())
    a.append(v * p)

l = list(accumulate(a))

for idx, _a in enumerate(l):
    if _a > X * 100:
        print(idx + 1)
        exit()
print("-1")
