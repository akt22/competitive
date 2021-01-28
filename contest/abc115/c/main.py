N, K = map(int, input().split())
H = [int(input()) for _ in range(N)]

H.sort()

ans = 10**10
for i in range(N - K + 1):
    diff = H[i + K - 1] - H[i]
    if diff == 0:
        print(0)
        exit()
    ans = min(ans, diff)
print(ans)
