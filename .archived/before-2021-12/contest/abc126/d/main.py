from collections import defaultdict, deque

N = int(input())

g = defaultdict(dict)
for _ in range(N - 1):
    u, v, w = list(map(int, input().split()))
    u, v = u - 1, v - 1
    g[u][v] = w
    g[v][u] = w


visited = [-1] * N
for i in range(N):
    if visited[i] != -1:
        continue

    q = deque()
    q.append((i, 0))
    visited[i] = 0
    while q:
        dep, color = q.popleft()
        for dest, cost in g[dep].items():
            if visited[dest] != -1:
                continue
            q.append((dest, (cost + color) % 2))
            visited[dest] = (cost + color) % 2
print(*visited, sep="\n")
