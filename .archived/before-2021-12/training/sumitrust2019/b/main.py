from math import ceil, floor

N = int(input())

x = N * 100. / 108.
c, f = ceil(x), floor(x)
if c == f:
    print(c)
    exit()
if N == int(c * 1.08):
    print(c)
elif N == int(f * 1.08):
    print(f)
else:
    print(":(")
