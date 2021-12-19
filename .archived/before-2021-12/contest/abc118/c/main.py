from math import gcd

N = int(input())
hp = list(map(int, input().split()))

ans = min(hp)
for h in hp:
    ans = min(ans, gcd(ans, h))
print(ans)
