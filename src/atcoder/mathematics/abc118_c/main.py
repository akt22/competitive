N = int(input())
a = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


ans = 0
for _a in a:
    ans = gcd(ans, _a)
print(ans)
