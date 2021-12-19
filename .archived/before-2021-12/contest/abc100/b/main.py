D, N = map(int, input().split())

p = 100**D

ans = 0
for i in range(1, N + 1):
    if i % 100 == 0:
        ans += p
    ans += p
print(ans)
