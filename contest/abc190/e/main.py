from collections import defaultdict, deque

N, M = map(int, input().split())

g = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

# INF = 10**9
# d = [[INF] * (N + 1) for _ in range(N + 1)]
# for _ in range(M):
#     a, b = map(int, input().split())
#     d[a][b] = 1
#     d[b][a] = 1


K = int(input())
stones = list(map(int, input().split()))

init = stones[0]

stones = set(stones)
q = deque()
q.append([init, 1, set(), set()])

while q:
    cur, cost, visited, seen = q.popleft()
    seen.add(cur)
    visited.add(cur)

    # print(f"{cur=}, {cost=}, {new=}, {seen=}")
    if len(visited) > M + 1:
        break
    if len(stones - seen) == 0:
        print(cost)
        exit()
    for dest in g[cur]:
        if dest not in visited:
            q.append([dest, cost + 1, set(), set(seen)])
print("-1")


# for k in range(N + 1):
#     for i in range(N + 1):
#         for j in range(N + 1):
#             d[i][j] = min(d[i][j], d[i][k] + d[k][j])

# ans = 1
# # dep = stones[0]
# for dest in stones[1:]:
#     # print(f"{dep=}, {dest=},{d[dep][dest]=}")
#     dist = d[init][dest]
#     if dist == INF:
#         print("-1")
#         exit()
#     ans += dist
#     dep = dest
# print(ans)
