from collections import defaultdict, deque

N, M = list(map(int, input().split()))
g = defaultdict(dict)
for _ in range(M):
    a, b, c = list(map(int, input().split()))
    a, b = a - 1, b - 1
    g[a][b] = c
    g[b][a] = c


INF = 1 << 60
forwards = [INF] * N

q = deque()
q.append([0, 0])
forwards[0] = 0
while q:
    dep, cost = q.popleft()
    for dest, dist in g[dep].items():
        if forwards[dest] > dist + cost:
            forwards[dest] = dist + cost
            q.append([dest, dist + cost])

backwards = [INF] * N

q = deque()
q.append([N - 1, 0])
backwards[N - 1] = 0
while q:
    dep, cost = q.popleft()
    for dest, dist in g[dep].items():
        if backwards[dest] > dist + cost:
            backwards[dest] = dist + cost
            q.append([dest, dist + cost])

for i in range(N):
    print(forwards[i] + backwards[i])
