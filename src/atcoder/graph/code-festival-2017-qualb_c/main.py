from collections import defaultdict, deque

N, M = map(int, input().split())
g = defaultdict(list)

for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

# is_bipartite template
color = [-1 for _ in range(N)]

q = deque()

color[0] = 1
q.append(0)
is_bipartite = True

while q:
    p = q.popleft()
    for dest in g[p]:
        if color[dest] == -1:
            color[dest] = (color[p] + 1) % 2
            q.append(dest)
        elif color[dest] == color[p]:
            is_bipartite = False
            break

if is_bipartite:
    B = color.count(1)
    W = len(color) - B
    print(B * W - M)
else:
    print(N * (N - 1) // 2 - M)
