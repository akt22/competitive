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


ans = 0
for i in range(1, N + 1, 2):
    if len(enum_divisors(i)) == 8:
        ans += 1
print(ans)
