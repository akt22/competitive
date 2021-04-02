N = int(input())

if N == 1:
    print(0)
    exit()
elif N == 2:
    print(2)
    exit()


MOD = 10**9 + 7

ans = pow(10, N, MOD) - pow(9, N, MOD) - pow(9, N, MOD) + pow(8, N, MOD)

print(ans % MOD)
