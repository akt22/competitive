N = int(input())


def enum_divisors(n):
    res = []
    i = 0
    while i * i <= N:
        i += 1
        if n % i == 0:
            res.append(i)
            if n // i != i:
                res.append(n // i)
    return sorted(set(res))


cnt = 0
for i in range(3, N + 1):
    if i % 2 == 0:
        continue
    d = enum_divisors(i)
    if len(d) == 8:
        cnt += 1
print(cnt)
