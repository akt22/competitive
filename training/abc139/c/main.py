N = int(input())

H = list(map(int, input().split()))

ans = 0
prev = H[0]
cnt = 0
for h in H[1:]:
    if prev >= h:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
    prev = h
ans = max(cnt, ans)
print(ans)
