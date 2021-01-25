N = int(input())

info = []
for _ in range(N):
    x, y, h = map(int, input().split())
    if h != 0:
        info.append([x, y, h])

if len(info) == 1:
    print(*info[0])
    exit()

ans_h = 10**10
ans_cx, ans_cy = 0, 0
for cx in range(101):
    for cy in range(101):
        flg = False
        H = 10**10
        for x, y, h in info:
            if flg:
                continue
            if H == 10**10:
                H = h + abs(cx - x) + abs(cy - y)
            else:
                H_cand = h + abs(cx - x) + abs(cy - y)
                if H != H_cand:
                    flg = True
        if not flg:
            ans_h, ans_cx, ans_cy = H, cx, cy
            break
print(ans_cx, ans_cy, ans_h)
