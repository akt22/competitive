from math import gcd

N = int(input())

T = [int(input()) for _ in range(N)]


ans = T[0]
for t in T:
    ans = t // gcd(ans, t) * ans
print(int(ans))
