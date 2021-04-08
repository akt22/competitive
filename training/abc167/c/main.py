from collections import defaultdict

N, M, X = list(map(int, input().split()))
C, A = [], []
for idx in range(N):
    l = list(map(int, input().split()))
    C.append(l[0])
    A.append(l[1:])

INF = 1 << 60
ans = INF
for i in range(2**N):
    tmp = defaultdict(int)
    tmp_c = 0
    for j in range(N):
        if (i >> j) & 1:
            for idx, a in enumerate(A[j]):
                tmp[idx] += a
            tmp_c += C[j]
    if tmp_c > 0 and all([v >= X for v in tmp.values()]):
        ans = min(tmp_c, ans)
if ans == INF:
    print(-1)
else:
    print(ans)
