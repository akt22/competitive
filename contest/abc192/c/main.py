N, K = list(map(int, input().split()))
raw = str(N)


def f(s):
    return str(int(s[::-1]) - int(s))


s = "".join(sorted(list(raw)))
for _ in range(K):
    raw = f(s)
    s = "".join(sorted(list(raw)))
print(raw)
