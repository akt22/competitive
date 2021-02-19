N = int(input())
water = list(map(int, input().split()))

sums = sum(water)

tmp = 0
for i in range(1, N, 2):
    tmp += water[i]
x = sums - 2 * tmp

ans = []
for a in water:
    ans.append(x)
    x = 2 * a - x
ans.append(x)
print(*ans[:-1])
