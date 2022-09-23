N, S = list(map(int, input().split()))
A = list(map(int, input().split()))

dp = [[False] * (S + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(1, N + 1):
    for j in range(S + 1):
        if j < A[i - 1]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j] or dp[i - 1][j - A[i - 1]]

if not dp[N][S]:
    print(-1)
    exit()

ans = []
acc = S
for pos in range(N, 0, -1):
    # pos-1ではaccにならなくて、posでaccになる → posのカードが選ばれている
    if not dp[pos - 1][acc] and dp[pos][acc]:
        ans.append(pos)
        acc -= A[pos - 1]

print(len(ans))
print(*ans[::-1])
