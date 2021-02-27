from collections import defaultdict

N, M = list(map(int, input().split()))
g = defaultdict(list)
for _ in range(M):
    a, b = list(map(int, input().split()))
    g[a].append(b)
    g[b].append(a)

transits = set(g[N])
transitables = set(g[1])

if len(transitables & transits) != 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
