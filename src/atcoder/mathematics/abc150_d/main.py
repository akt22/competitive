from math import gcd

N, M = map(int, input().split())
a = list(map(int, input().split()))


b = list(map(lambda x: x // 2, a))


def prime_factorize(n):
    ret = 0
    i = 2
    if n % i != 0:
        return 0
    while n % i == 0:
        ret += 1
        n //= i
    return ret


check = set([prime_factorize(_b) for _b in b])
if len(check) != 1:
    print(0)
    exit()

l = 1
for _b in b:
    g = gcd(l, _b)
    l = l // g * _b

print((M // l + 1) // 2)
