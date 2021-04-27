B, C = list(map(int, input().split()))


def f(c):
    if c == 0:
        return (0, 0)
    n = c // 2
    return (B - n, B + n - 1) if c % 2 == 0 else (-B - n, -B + n)


(a, b) = f(C)
(c, d) = f(C - 1)
ans = (b - a + 1) + (d - c + 1) - max(0, min(b, d) - max(a, c) + 1)
print(ans)
