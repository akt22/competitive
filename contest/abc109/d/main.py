H, W = map(int, input().split())

A = []
for _ in range(H):
    row = list(map(int, input().split()))
    A.append(row)

cnt = 0
ans = []
for h in range(H):
    for w in range(W - 1):
        if A[h][w] % 2 == 1:
            ans.append([h + 1, w + 1, h + 1, w + 2])
            A[h][w + 1] += 1

for h in range(H - 1):
    if A[h][W - 1] % 2 == 1:
        ans.append([h + 1, W, h + 2, W])
        A[h + 1][W - 1] += 1

print(len(ans))
for ope in ans:
    print(*ope)
