N, M, Q = map(int, input().split())


trains = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    l, r = map(int, input().split())
    trains[l][r] += 1

questions = [list(map(int, input().split())) for _ in range(Q)]

acc = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N + 1):
    for j in range(N + 1):
        acc[i][j] = acc[i][j - 1] + trains[i][j]

for p, q in questions:
    ans = 0
    for i in range(p, q + 1):
        ans += acc[i][q]
    print(ans)
