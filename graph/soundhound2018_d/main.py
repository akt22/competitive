from collections import defaultdict, deque

n, m, s, t = map(int, input().split())
s, t = s - 1, t - 1
g = defaultdict(dict)

hand = 10**15

for _ in range(m):
    u, v, a, b = map(int, input().split())
    u, v = u - 1, v - 1
    g[u][v] = [a, b]
    g[v][u] = [a, b]


def dijkstra(s, cost_idx, d):
    q = deque()
    q.append((0, s))
    d[s] = 0
    while q:
        cost, p = q.popleft()
        if d[p] < cost:
            continue
        for i in g[p]:
            dis = g[p][i][cost_idx]
            if d[i] > d[p] + dis:
                d[i] = d[p] + dis
                q.append((d[i], i))


d0 = [10**16 for _ in range(n)]
dijkstra(s, 0, d0)
d1 = [10**16 for _ in range(n)]
dijkstra(t, 1, d1)

ans = [0 for _ in range(n)]
for i in range(n):
    hand = min(hand, d0[n - 1 - i] + d1[n - 1 - i])
    ans[n - 1 - i] = 10**15 - hand

for a in ans:
    print(a)
