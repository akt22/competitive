N = int(input())
A = [0, 0] + list(map(int, input().split()))
B = [0, 0, 0] + list(map(int, input().split()))

dp = [0] * (N + 1)
dp[2] = A[2]

step = [0, 0, 1]

for i in range(3, N + 1):
    left = dp[i - 1] + A[i]
    right = dp[i - 2] + B[i]
    if left < right:
        step.append(i - 1)
        dp[i] = left
    else:
        step.append(i - 2)
        dp[i] = right

ans = [N]

i = N
while i > 1:
    prev = step[i]
    ans.append(prev)
    i = prev

print(len(ans))
ans.reverse()
print(*ans, sep=" ")
