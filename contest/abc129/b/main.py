N = int(input())
W = list(map(int, input().split()))

INF = 1 << 60
ans = INF
for i in range(0, N - 1):
    s1 = sum(W[:i + 1])
    s2 = sum(W[i + 1:])
    ans = min(ans, abs(s1 - s2))
print(ans)
