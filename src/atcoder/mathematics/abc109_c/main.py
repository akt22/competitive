N, X = map(int, input().split())
x = list(map(lambda x: abs(X - int(x)), input().split()))


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


res = 0
for _x in x:
    res = gcd(res, _x)
print(res)
