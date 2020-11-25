import sys
sys.setrecursionlimit(2**15)

N, X = map(int, input().split())


def rec(a, b):
    if a > b:
        a, b = b, a

    tmp = int(b / a)
    if b % a == 0:
        return (2 * tmp - 1) * a
    else:
        return 2 * tmp * a + rec(b % a, a)


print(N + rec(X, N - X))
