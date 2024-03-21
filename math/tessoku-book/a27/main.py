A, B = list(map(int, input().split()))


def gcd(a, b):
    while a >= 1 and b >= 1:
        if a >= b:
            a %= b
        else:
            b %= a
    return a if a != 0 else b


print(gcd(A, B))
