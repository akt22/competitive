from math import gcd

A, B = map(int, input().split())

g = gcd(A, B)


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


d = prime_factorize(g)
print(len(d) + 1)
