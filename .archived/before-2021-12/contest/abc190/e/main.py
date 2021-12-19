from collections import defaultdict, deque

N, M = map(int, input().split())

g = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append(b)
    g[b].append(a)


K = int(input())
stones = list(map(lambda x: int(x) - 1, input().split()))

INF = 10**10


def bfs(sv):
    dist = [INF] * N
    q = deque()
    dist[sv] = 0
    q.append(sv)
    while q:
        v = q.popleft()
        for u in g[v]:
            if dist[u] != INF:
                continue
            q.append(u)
            dist[u] = dist[v] + 1
    return dist


dist = defaultdict(dict)
for i in range(K):
    d = bfs(stones[i])
    for j in range(K):
        dist[i][j] = d[stones[j]]

dp = [[INF] * K for _ in range(2**K)]
for i in range(K):
    dp[2**i][i] = 1

for s in range(2**K):
    for i in range(K):
        if not ((s >> i) & 1):
            continue
        for j in range(K):
            if (s >> j) & 1:
                continue
            dp[s | 1 << j][j] = min(dp[s | 1 << j][j], dp[s][i] + dist[i][j])

ans = min(dp[2**K - 1])
if ans == INF:
    print("-1")
else:
    print(ans)
