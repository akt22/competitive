from collections import deque, defaultdict

N = int(input())

g = defaultdict(dict)
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    g[u][v] = w
    g[v][u] = w

visited = [-1 for _ in range(N)]

q = deque()

for i in range(1, N + 1):
    if visited[i - 1] != -1:
        continue
    q.append((i, 0))
    while q:
        p, w = q.popleft()
        visited[p - 1] = w % 2

        dests = g[p]
        for dest, dist in dests.items():
            if visited[dest - 1] != -1:
                continue
            q.append((dest, w + dist))

for i in visited:
    print(i)
