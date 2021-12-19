N, M = map(int, input().split())


def enum_divisors(n):
    res = []
    i = 0
    while i * i <= n:
        i += 1
        if n % i == 0:
            res.append(i)
            if n // i != i:
                res.append(n // i)
    return sorted(set(res))


divisors = enum_divisors(M)
ans = 0
for divisor in divisors:
    if divisor > M // N:
        break
    ans = divisor
print(ans)
