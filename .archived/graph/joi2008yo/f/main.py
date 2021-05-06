from collections import defaultdict, deque

n, k = map(int, input().split())

g = defaultdict(dict)
INF = 10**9


def append(c, d, e):
    g[c][d] = min(g[c].get(d, INF), e)
    g[d][c] = min(g[d].get(c, INF), e)


def answer(a, b):
    q = deque()
    q.append([a, 0])
    visited = [INF] * (n + 1)
    while q:
        dep, current_cost = q.popleft()
        for dest, cost in g[dep].items():
            if visited[dest] > (current_cost + cost):
                visited[dest] = current_cost + cost
                q.append([dest, current_cost + cost])

    if visited[b] == INF:
        print(-1)
    else:
        print(visited[b])


for _ in range(k):
    info = list(map(int, input().split()))
    if info[0] == 1:
        append(*info[1:])
    else:
        answer(*info[1:])
