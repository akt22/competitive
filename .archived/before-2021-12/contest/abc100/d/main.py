N, M = map(int, input().split())

cakes = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(2**3):
    l = [0] * N
    for j in range(3):
        s = 1 if (i >> j) & 1 else -1
        l = [l[i] + s * cakes[i][j] for i in range(N)]
    l.sort(reverse=True)
    ans = max(sum(l[:M]), ans)
print(ans)
