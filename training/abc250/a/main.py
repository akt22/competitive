H, W = list(map(int, input().split()))
R, C = list(map(int, input().split()))

ans = 0
if R - 1 > 0:
    ans += 1
if R + 1 <= H:
    ans += 1
if C - 1 > 0:
    ans += 1
if C + 1 <= W:
    ans += 1
print(ans)
