from collections import defaultdict, deque

N, M = list(map(int, input().split()))
g = defaultdict(dict)
for _ in range(M):
    a, b, c = list(map(int, input().split()))
    a, b = a - 1, b - 1
    g[a][b] = c
    g[b][a] = c

INF = 1 << 60


def dijkstra(s):
    costs = [INF] * N
    q = deque()
    q.append([s, 0])
    costs[s] = 0
    while q:
        dep, cost = q.popleft()
        for dest, dist in g[dep].items():
            if costs[dest] > cost + dist:
                q.append([dest, cost + dist])
                costs[dest] = cost + dist
    return costs


forward = dijkstra(0)
backward = dijkstra(N - 1)

for i in range(N):
    print(forward[i] + backward[i])
