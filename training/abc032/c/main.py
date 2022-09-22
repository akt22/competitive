N, K = list(map(int, input().split()))

S = []
for _ in range(N):
    i = int(input())
    if i == 0:
        print(N)
        exit()
    S.append(i)

ans = 0
right = 0

mul = 1
for left in range(N):
    while right < N and mul * S[right] <= K:
        mul *= S[right]
        right += 1
    ans = max(ans, right - left)
    if left == right:
        right += 1
    else:
        mul /= S[left]
print(ans)
