N = int(input())
shops = [list(map(int, input().split())) for _ in range(N)]

INF = 1 << 60
ans = INF

for idx, (a, p, x) in enumerate(shops):
    remain = x - a
    if remain <= 0:
        continue
    ans = min(p, ans)

print(ans if ans != INF else -1)
