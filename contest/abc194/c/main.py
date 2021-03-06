N = int(input())
A = list(map(int, input().split()))


ans = 0
sums = 0
for a in A:
    ans += a**2
    sums += a
ans *= (N - 1)

m = 0
for a in A:
    m += (a * (sums - a))
print(ans - m)
