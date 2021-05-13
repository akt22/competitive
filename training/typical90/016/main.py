N = int(input())
A, B, C = sorted(list(map(int, input().split())))

INF = 1 << 60
ans = INF
for c in range(N):
    if c * C > N:
        break
    for b in range(N):
        if c * C + b * B > N:
            break
        aA = N - (c * C + b * B)
        if aA % A == 0:
            a = aA // A
            ans = min(ans, a + b + c)
print(ans)
