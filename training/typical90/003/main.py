from collections import defaultdict, deque

N = int(input())
g = defaultdict(list)
for _ in range(N - 1):
    a, b = list(map(int, input().split()))
    g[a].append(b)
    g[b].append(a)


q = deque()
visited = [-1] * (N + 1)
visited[1] = 0
q.append([1, 0])
while q:
    dep, cost = q.popleft()
    for dest in g[dep]:
        if visited[dest] == -1:
            q.append([dest, cost + 1])
            visited[dest] = cost + 1

farthest = 0
max_cost = 0
for idx, c in enumerate(visited):
    if c > max_cost:
        farthest = idx
        max_cost = c

q = deque()
visited = [-1] * (N + 1)
visited[farthest] = 0
q.append([farthest, 0])
while q:
    dep, cost = q.popleft()
    for dest in g[dep]:
        if visited[dest] == -1:
            q.append([dest, cost + 1])
            visited[dest] = cost + 1
print(max(visited) + 1)
