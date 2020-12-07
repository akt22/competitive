N = int(input())

market = [list(map(int, input().split())) for _ in range(N)]

ans = 10**15
for s, _ in market:
    for _, t in market:
        total = 0
        for a, b in market:
            dist = abs(s - a) + abs(a - b) + abs(b - t)
            total += dist
        ans = min(ans, total)
print(ans)
