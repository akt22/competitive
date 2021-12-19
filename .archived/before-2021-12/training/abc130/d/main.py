from itertools import accumulate

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

sums = list(accumulate(A))
sums.insert(0, 0)

ans, cur = 0, 0
for i in range(N + 1):
    if sums[i] >= K:
        for j in range(cur, i + 1):
            if sums[i] - sums[j] < K:
                ans += j
                cur = j
                break
print(ans)
