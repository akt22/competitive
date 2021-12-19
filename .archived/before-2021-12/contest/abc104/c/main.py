D, G = map(int, input().split())

P, C = [], []
for _ in range(D):
    p, c = map(int, input().split())
    P.append(p)
    C.append(c)


ans = 10**10
for i in range(2**D):
    score, cnt, rest = 0, 0, 0
    for j in range(D):
        if (i >> j) & 1:
            score += 100 * (j + 1) * P[j] + C[j]
            cnt += P[j]
        else:
            rest = j

    if G > score:
        base = (rest + 1) * 100
        shortage = ((G - score - 1) // base) + 1
        if P[rest] <= shortage:
            continue
        cnt += shortage

    ans = min(ans, cnt)
print(ans)
