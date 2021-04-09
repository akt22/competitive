L, R = list(map(int, input().split()))

p = 2019

INF = 1 << 60
ans = INF
for i in range(L, R + 1):
    for j in range(i + 1, R + 1):
        mod = (i * j) % p
        ans = min(ans, mod)
        if mod == 0:
            print(0)
            exit()
print(ans)
