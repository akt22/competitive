from collections import defaultdict

N, M = list(map(int, input().split()))
g = defaultdict(list)
for _ in range(M):
    u, v = list(map(int, input().split()))
    g[u].append(v)
    g[v].append(u)


ans = 0


def dps(start, depth, current):
    cnt = 0
    if depth == 3 and start == current:
        return 1
    if depth == 3:
        return 0
    for i in g[current]:
        cnt += dps(start, depth + 1, i)
    return cnt


for i in range(1, N + 1):
    ans += dps(i, 0, i)

print(ans // 6)
