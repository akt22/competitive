D, N = list(map(int, input().split()))
query = [list(map(int, input().split())) for _ in range(N)]

cond = [24] * D
for l, r, h in query:
    for i in range(l - 1, r):
        cond[i] = min(cond[i], h)
print(sum(cond))
