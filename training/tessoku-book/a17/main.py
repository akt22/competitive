N = int(input())
A = [0] + list(map(int, input().split()))
B = [0, 0] + list(map(int, input().split()))

dp = [0] * N
dp[1] = A[1]

for i in range(2, N):
    dp[i] = min(dp[i - 2] + B[i], dp[i - 1] + A[i])

ans = []
pos = N - 1
while True:
    ans.append(pos + 1)
    if pos == 0:
        break
    if dp[pos - 1] + A[pos] == dp[pos]:
        pos -= 1
    else:
        pos -= 2
print(len(ans))
print(*reversed(ans))
