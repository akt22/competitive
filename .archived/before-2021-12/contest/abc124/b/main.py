N = int(input())
heights = list(map(int, input().split()))

ans = 1
highest = heights[0]

for h in heights[1:]:
    if h >= highest:
        ans += 1
        highest = h
print(ans)
