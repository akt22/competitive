from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)


N, Q = map(int, input().split())
tree = defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    tree[a].append(b)
    tree[b].append(a)

ans = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    ans[p - 1] += x


def dfs(c, p):
    for n in tree[c]:
        if n == p:
            continue
        ans[n] += ans[c]
        dfs(n, c)


dfs(0, -1)
print(*ans)
