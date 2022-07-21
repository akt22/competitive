N, L = list(map(int, input().split()))
K = int(input())
A = list(map(int, input().split()))


def cuttable(m):
    span, cnt = 0, 0
    for a in A:
        if a - span >= m and L - a >= m:
            cnt += 1
            span = a
    return True if cnt >= K else False


l, r = -1, L + 1
while l + 1 < r:
    m = (l + r) // 2
    if cuttable(m):
        l = m
    else:
        r = m
print(l)
