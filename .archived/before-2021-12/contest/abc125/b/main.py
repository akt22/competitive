N = int(input())
values = list(map(int, input().split()))
costs = list(map(int, input().split()))

ans = 0
for i in range(2**N):
    x, y = 0, 0
    for j in range(N):
        if (i >> j) & 1:
            x += values[j]
            y += costs[j]
    ans = max(ans, x - y)
print(ans)
