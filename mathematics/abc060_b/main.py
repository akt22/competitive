A, B, C = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


g = gcd(A, B)
if C % g == 0:
    print("YES")
else:
    print("NO")
