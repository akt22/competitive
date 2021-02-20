N, K = list(map(int, input().split()))
str_N = str(N)


def f(s):
    return str(int(s[::-1]) - int(s))


raw = str_N
s = "".join(sorted(list(str_N)))
for k in range(K):
    raw = f(s)
    new = "".join(sorted(list(raw)))
    s = new
print(raw)
