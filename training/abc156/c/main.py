N = int(input())
X = list(map(int, input().split()))

INF = 1 << 60
ans = INF
for i in range(1, 100):
    tmp = 0
    for x in X:
        tmp += (x - i) ** 2
    ans = min(ans, tmp)
print(ans)
