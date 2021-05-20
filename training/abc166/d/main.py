X = int(input())


def enum_divisors(n):
    res = {}
    i = 0
    while i * i <= n:
        i += 1
        if n % i == 0:
            res[i] = n // i
    return res


d = enum_divisors(X)

a = 0
while a ** 2 <= X:
    for x, y in d.items():
        b = a - x
        if a ** 5 - b ** 5 == X:
            print(a, b)
            exit()
    a += 1
