N = int(input())
A = list(map(int, input().split()))

ans = 0
for idx, a in enumerate(A):
    tmp = a
    candidate = []
    min_value = a
    for idx2, _a in enumerate(A[(idx + 1):]):
        if min_value > _a:
            if tmp > ans:
                candidate.append(tmp)
            min_value = _a
            tmp = _a * (idx2 + 2)
        else:
            tmp += min_value
    # print(f"{idx=}, {ans=}, {tmp=}")
    ans = max(ans, tmp)
    for c in candidate:
        ans = max(ans, c)
print(ans)
