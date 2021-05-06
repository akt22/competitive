from collections import defaultdict, deque

N, M = list(map(int, input().split()))
g = defaultdict(list)
for _ in range(M):
    a, b = list(map(int, input().split()))
    a, b = a - 1, b - 1
    g[a].append(b)
    g[b].append(a)


q = deque()
visited = [-1] * N
is_bipartite = True
for i in range(N):
    if not is_bipartite:
        break
    if visited[i] != -1:
        continue
    q.append([i, 0])
    visited[i] = 0
    while q:
        dep, color = q.popleft()
        for dest in g[dep]:
            if visited[dest] == -1:
                q.append([dest, int(not color)])
                visited[dest] = int(not color)
            elif visited[dest] == color:
                is_bipartite = False
                break

if not is_bipartite:
    print(((N * (N - 1)) // 2) - M)
else:
    print(visited.count(0) * visited.count(1) - M)
