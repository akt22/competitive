from collections import defaultdict, deque

N, M, T = map(int, input().split())
revenues = list(map(int, input().split()))

g1 = defaultdict(dict)
g2 = defaultdict(dict)

for _ in range(M):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    g1[a][b] = c
    g2[b][a] = c


def dijkstra(s, g, d):
    q = deque()
    q.append((0, s))
    d[s] = 0
    while q:
        cost, p = q.popleft()
        if d[p] < cost:
            continue
        for i in g[p]:
            dis = g[p][i]
            if d[i] > d[p] + dis:
                d[i] = d[p] + dis
                q.append((d[i], i))


s = 0

INF = 10**16
inbounds = [INF for _ in range(N)]
dijkstra(s, g1, inbounds)

outbounds = [INF for _ in range(N)]
dijkstra(s, g2, outbounds)

ans = T
for idx, (inbound, outbound) in enumerate(zip(inbounds, outbounds)):
    if ans < inbound + outbound:
        continue
    sec = T - (inbound + outbound)
    ans = max(ans, sec * revenues[idx])

print(ans)
