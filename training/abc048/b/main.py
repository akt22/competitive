a, b, x = list(map(int, input().split()))


def f(n): return n // x + 1 if n != -1 else 0


ans = f(b) - f(a - 1)
print(ans)
