N = int(input())
H = map(int, input().split())


ans = 0
cur = 0
for h in H:
    if h > cur:
        ans += h - cur
    cur = h
print(ans)
