N = int(input())


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
d = prime_factorize(N)
for k, v in d.items():
    i = 0
    sums = 0
    while True:
        i += 1
        if v < sums + i:
            break
        sums += i
        ans += 1
print(ans)
