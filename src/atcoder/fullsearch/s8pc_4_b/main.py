N, K = map(int, input().split())
heights = list(map(int, input().split()))

ans = 10**20
for i in range(2**N):
    fee = 0
    cnt = 0
    highest = 0
    for j in range(N):
        if (i >> j) & 1:
            cnt += 1
            if highest >= heights[j]:
                fee += highest - heights[j] + 1
                highest += 1

        highest = max(highest, heights[j])

    if cnt >= K:
        ans = min(ans, fee)
print(ans)
