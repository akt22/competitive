from collections import defaultdict, deque
from math import inf

N, M, K, S = map(int, input().split())
P, Q = map(int, input().split())


dominated = {}

for _ in range(K):
    d = int(input()) - 1
    dominated[d] = True

g = defaultdict(list)
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

dangerous = set()
d = dominated.keys()
while S > 0:
    for t in d:
        for i in g[t]:
            dangerous.add(i)
    d = list(dangerous)
    S -= 1


q = deque()
q.append([0, 0])

visited = [inf] * (N)

while q:
    dep, current_cost = q.popleft()
    for dest in g[dep]:
        if dest in dominated:
            continue
        if dest == N - 1:
            visited[dest] = min(visited[dest], current_cost)
            continue
        cost = Q if dest in dangerous else P
        if visited[dest] > (cost + current_cost):
            visited[dest] = cost + current_cost
            q.append([dest, cost + current_cost])

print(visited[N - 1])
