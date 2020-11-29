from math import sqrt

N, P = map(int, input().split())


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if i != 2 and i % 2 == 0:
            continue
        if n % i == 0:
            return False
    return True


def prime_factorize(n):
    d = {}
    i = 1
    while i**2 <= n:
        i += 1
        if n % i != 0:
            continue
        d[i] = 0
        while n % i == 0:
            d[i] += 1
            n //= i
    if n != 1:
        d[n] = 1
    return d


d = prime_factorize(P)

ans = 1
for k, v in d.items():
    for i in range(v // N):
        ans *= k

print(ans)
