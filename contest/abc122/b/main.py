S = input()

base = set(["A", "C", "G", "T"])
ans = 0
for idx, start in enumerate(S):
    if start not in base:
        continue
    cnt = 1
    flg = True
    for s in S[idx + 1:]:
        if s in base and flg:
            cnt += 1
        else:
            flg = False
    ans = max(ans, cnt)
print(ans)
