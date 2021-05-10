from collections import defaultdict, deque

N, M = list(map(int, input().split()))
g = defaultdict(list)

for _ in range(M):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    g[a].append(b)
    g[b].append(a)

q = deque()
q.append([0, 0])

INF = 1 << 60
costs = [INF] * N
costs[0] = 0

deps = [N + 1] * N
deps[0] = 0

while q:
    dep, cost = q.popleft()
    for dest in g[dep]:
        if costs[dest] > cost + 1:
            costs[dest] = cost + 1
            deps[dest] = dep + 1
            q.append([dest, cost + 1])

print("Yes")
print(*deps[1:], sep="\n")
