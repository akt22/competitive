from math import floor

N = int(input())

if N % 2 == 1:
    print(0)
    exit()

ans = 0
p = 10
while p <= N:
    ans += floor(N // p)
    p *= 5
print(ans)
