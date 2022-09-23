N = int(input())
H = list(map(int, input().split()))

dp = [0] * N
dp[1] = abs(H[1] - H[0])

for i in range(2, N):
    dp[i] = min(dp[i - 2] + abs(H[i] - H[i - 2]), dp[i - 1] + abs(H[i] - H[i - 1]))

ans = []
pos = N - 1
while True:
    ans.append(pos + 1)
    if pos <= 0:
        break
    if dp[pos] == dp[pos - 1] + abs(H[pos] - H[pos - 1]):
        pos -= 1
    else:
        pos -= 2
print(len(ans))
print(*reversed(ans))
