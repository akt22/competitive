N = int(input())

bonus = [input().split() for _ in range(N)]

ans = 0.0
for x, u in bonus:
    if u == "JPY":
        ans += float(x)
    else:
        ans += float(x) * 380000.0
print(ans)
