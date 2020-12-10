R, C = map(int, input().split())

crackers = [list(map(lambda x: x == "1", input().split())) for _ in range(R)]

ans = 0
for i in range(2**R):
    flipped_row = {}
    baked = 0
    for j in range(R):
        flipped_row[j] = (i >> j) & 1

    for j in range(C):
        cnt = 0
        for k in range(R):
            cnt += flipped_row[k] ^ crackers[k][j]
        baked += max(cnt, R - cnt)
    ans = max(ans, baked)
print(ans)
