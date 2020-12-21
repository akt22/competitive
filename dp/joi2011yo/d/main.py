N = int(input())
numbers = list(map(int, input().split()))
target = numbers[-1]

dp = [[0] * 21 for _ in range(N - 1)]
dp[0][numbers[0]] = 1

for i in range(1, N - 1):
    number = numbers[i]
    for j in range(21):
        k = j + number
        if 0 <= k <= 20:
            dp[i][k] += dp[i - 1][j]
        k = j - number
        if 0 <= k <= 20:
            dp[i][k] += dp[i - 1][j]

print(dp[N - 2][target])
