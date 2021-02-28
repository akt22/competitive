from itertools import accumulate

N, W = list(map(int, input().split()))
plans = [list(map(int, input().split())) for _ in range(N)]

d = [0] * (2 * (10**5) + 1)

for s, t, p in plans:
    d[s] += p
    d[t] -= p

if max(accumulate(d)) > W:
    print("No")
else:
    print("Yes")
