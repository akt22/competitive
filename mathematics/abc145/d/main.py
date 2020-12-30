X, Y = map(int, input().split())

MOD = 10**9 + 7


def comb(n, r, mod):
    r = min(n - r, r)
    if r == 0:
        return 1
    x, y = 1, 1
    for i in range(1, r + 1):
        x = x * (n + 1 - i) % mod
        y = y * i % mod
    return x * pow(y, mod - 2, mod) % mod


if (X + Y) % 3 != 0:
    print(0)
    exit()

n = ((-1 * X) + (2 * Y)) // 3
m = ((2 * X) + (-1 * Y)) // 3

if n < 0 or m < 0:
    print(0)
    exit()

print(comb(n + m, n, MOD))
