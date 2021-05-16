N = int(input())
xy = {}
for i in range(N):
    a = int(input())
    xy[i + 1] = [list(map(int, input().split())) for _ in range(a)]

ans = 0
for i in range(2**N):
    honests = [False] * (N + 1)
    cand = 0
    for j in range(N):
        if (i >> j) & 1:
            honests[j + 1] = True
            cand += 1

    mentions = {}
    flg = True
    for k in range(1, N + 1):
        if flg and honests[k]:
            for x, y in xy[k]:
                if y == 0 and honests[x]:
                    flg = False
                    break
                elif y == 1 and not honests[x]:
                    flg = False
                    break
                elif x not in mentions:
                    mentions[x] = y
                elif mentions[x] == y:
                    continue
                else:
                    flg = False
                    break

    if flg:
        ans = max(ans, cand)
print(ans)
