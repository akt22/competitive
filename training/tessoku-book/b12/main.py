N = int(input())

l, r = 0., float(N)
for _ in range(30):
    m = (l + r) / 2.
    if m**3 + m == N:
        print(m)
        exit()
    elif m**3 + m < N:
        l = m
    else:
        r = m
print(m)
