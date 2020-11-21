from collections import defaultdict

N, M = map(int, input().split())
g = defaultdict(dict)

alist, blist, clist = [], [], []
for _ in range(M):
    a, b, c = map(int, input().split())
    alist.append(a)
    blist.append(b)
    clist.append(-c)

INF = 10**15
dist = [INF for _ in range(N)]

dist[0] = 0


for _ in range(N - 1):
    for a, b, c in (zip(alist, blist, clist)):
        if dist[a - 1 == INF]:
            continue
        if dist[b - 1] > dist[a - 1] + c:
            dist[b - 1] = dist[a - 1] + c

ans = dist[N - 1]

negative = [False for _ in range(N)]

for _ in range(N):
    for a, b, c, in zip(alist, blist, clist):
        if dist[a - 1] == INF:
            continue
        if dist[b - 1] > dist[a - 1] + c:
            dist[b - 1] = dist[a - 1] + c
            negative[b - 1] = True
        if negative[a - 1]:
            negative[b - 1] = True

if negative[N - 1]:
    print("inf")
else:
    print(-ans)
