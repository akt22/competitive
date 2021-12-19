import sys
N, X = map(int, input().split())

sys.setrecursionlimit(500000)


def f(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + a[n - 1]:
        return f(n - 1, x - 1)
    else:
        return p[n - 1] + 1 + f(n - 1, x - 2 - a[n - 1])


a, p = [1], [1]
for i in range(N):
    a.append(2 * a[i] + 3)
    p.append(2 * p[i] + 1)

print(f(N, X))
