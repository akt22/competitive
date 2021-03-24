from collections import defaultdict
from itertools import permutations

N, K = list(map(int, input().split()))

g = defaultdict(dict)
for i in range(N):
    for j, v in enumerate(list(map(int, input().split()))):
        g[i + 1][j + 1] = v

ans = 0
for p in permutations(list(range(2, N + 1))):
    tmp = 0
    dep = 1
    for dest in p:
        tmp += g[dep][dest]
        dep = dest
    tmp += g[dest][1]
    if K == tmp:
        ans += 1
print(ans)
