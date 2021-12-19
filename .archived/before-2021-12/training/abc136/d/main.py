S = input()

segments = []
continue_r = True
start = 0
idx = 0
gap = []
cnt_r, cnt_l = 0, 0
for idx, s in enumerate(S):
    if continue_r and s == "L":
        continue_r = False
        gap = [idx - 1, idx]
    elif not continue_r and s == "R":
        segments.append([gap, [cnt_r, cnt_l], S[start:idx]])
        continue_r = True
        start = idx
        cnt_r, cnt_l = 0, 0
    if s == "R":
        cnt_r += 1
    else:
        cnt_l += 1
# TODO: S = RLのときだけあとで調査
segments.append([gap, [cnt_r, cnt_l], S[start:idx + 1]])
# print(segments)

ans = [0] * len(S)
for gap, (cnt_r, cnt_l), seg in segments:
    cnt = cnt_r + cnt_l
    if (cnt) % 2 == 0:
        ans[gap[0]] = cnt // 2
        ans[gap[1]] = cnt // 2
    else:
        # TODO
        tmp = max(cnt_r, cnt_l)
        if cnt_r > cnt_l:
            if (cnt_r - 1) % 2 == 0:
                ans[gap[0]] = cnt // 2 + 1
                ans[gap[1]] = cnt // 2
            else:
                ans[gap[0]] = cnt // 2
                ans[gap[1]] = cnt // 2 + 1
        else:
            if (cnt_l - 1) % 2 == 0:
                ans[gap[0]] = cnt // 2
                ans[gap[1]] = cnt // 2 + 1
            else:
                ans[gap[0]] = cnt // 2 + 1
                ans[gap[1]] = cnt // 2
print(*ans)
