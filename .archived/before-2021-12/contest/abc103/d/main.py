from collections import defaultdict

N, M = map(int, input().split())

wishes = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

ans = 0
INF = 10**10
dropped = INF

for a, b in sorted(wishes, key=lambda x: x[1]):
    if dropped == INF or a >= dropped:
        dropped = b
        ans += 1
print(ans)
