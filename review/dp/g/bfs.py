from collections import defaultdict, deque

N, M = list(map(int, input().split()))
g = defaultdict(list)
deg = defaultdict(int)
for _ in range(M):
    x, y = list(map(int, input().split()))
    x, y = x - 1, y - 1
    g[x].append(y)
    deg[y] += 1

costs = [0] * N

q = deque()
for i in range(N):
    if i not in deg:
        q.append(i)
while q:
    dep = q.popleft()
    for dest in g[dep]:
        deg[dest] -= 1
        if deg[dest] == 0:
            q.append(dest)
            costs[dest] = max(costs[dest], costs[dep] + 1)
print(max(costs))
