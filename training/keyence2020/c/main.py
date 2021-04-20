N, K, S = list(map(int, input().split()))

remain = 1 if S + 1 > 10**9 else S + 1
ans = [S] * K + [remain] * (N - K)
print(*ans)
