from collections import defaultdict, deque
N, M = map(int, input().split())

g = defaultdict(dict)

for _ in range(M):
    a, b, t = map(int, input().split())
    a, b = a - 1, b - 1
    g[a][b] = t
    g[b][a] = t


INF = float('inf')
d = [[INF] * (N) for _ in range(N)]

for i in range(N):
    q = deque()
    q.append([i, 0])
    while q:
        frm, current_cost = q.popleft()
        for dest, cost in g[frm].items():
            if i == dest:
                continue
            estimated = current_cost + cost
            if d[i][dest] > estimated:
                d[i][dest] = estimated
                q.append([dest, estimated])

min_value = INF
for idx, cost in enumerate(d):
    del cost[idx]
    c = max(cost)
    min_value = min_value if min_value < c else c
print(min_value)
