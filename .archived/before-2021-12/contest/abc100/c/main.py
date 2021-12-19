N = int(input())
a = map(int, input().split())


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


ans = 0
for _a in a:
    if _a % 2 != 0:
        continue
    d = prime_factorize(_a)
    ans += d.get(2, 0)
print(ans)
