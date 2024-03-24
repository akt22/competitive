a, b = list(map(int, input().split()))

MOD = 10**9 + 7

# print(pow(a, b, MOD))

ans = 1
for i in range(30):
    wari = 2**i
    if (b // wari) % 2 == 1:
        ans = (ans * a) % MOD
    a = (a * a) % MOD


print(ans)
