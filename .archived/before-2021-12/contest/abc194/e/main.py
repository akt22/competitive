N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

cnt = [0] * N
ans = N
for i in range(M):
    cnt[A[i]] += 1
for i in range(N):
    if cnt[i] == 0:
        ans = i
        break

for i in range(N - M):
    cnt[A[i]] -= 1
    cnt[A[i + M]] += 1
    if cnt[A[i]] == 0:
        ans = min(ans, A[i])
print(ans)
