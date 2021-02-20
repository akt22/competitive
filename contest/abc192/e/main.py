from collections import defaultdict, deque
from math import ceil

N, M, X, Y = list(map(int, input().split()))
g = defaultdict(list)
for i in range(M):
    a, b, t, k = list(map(int, input().split()))
    g[a].append([b, t, k])
    g[b].append([a, t, k])


q = deque()
q.append([X, 0])
INF = 1 << 60
visited = [INF] * (N + 1)
visited[X] = 0
while q:
    dep, cost = q.popleft()
    if visited[dep] < cost:
        continue
    for dest, t, k in g[dep]:
        c = ceil(cost / k) * k + t
        if visited[dest] > c:
            q.append([dest, c])
            visited[dest] = c

print(visited[Y] if visited[Y] != INF else -1)
