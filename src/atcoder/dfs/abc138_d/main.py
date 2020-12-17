from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)


N, Q = map(int, input().split())
tree = defaultdict(list)
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    tree[a].append(b)

opes = []
for _ in range(Q):
    p, x = map(int, input().split())
    opes.append([p - 1, x])


def dfs(cost, ope):
    p, x = ope
    if p not in tree:
        cost[p] += x
        return cost
    for child in tree[p]:
        dfs(cost, [child, x])
    cost[p] += x


cost = defaultdict(int)
for ope in opes:
    dfs(cost, ope)

print(" ".join([str(cost[i]) for i in range(N)]))
