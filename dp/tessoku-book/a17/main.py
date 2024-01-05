N = int(input())
A = [0, 0] + list(map(int, input().split()))
B = [0, 0, 0] + list(map(int, input().split()))

dp = [0] * (N + 1)
dp[2] = A[2]

for i in range(3, N + 1):
    dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + B[i])

ans = [N]
idx = N

while idx > 1:
    idx = idx - 1 if dp[idx - 1] == dp[idx] - A[idx] else idx - 2
    ans.append(idx)

print(len(ans))
ans.reverse()
print(*ans, sep=" ")
