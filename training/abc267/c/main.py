N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

cur = sum(A[1:M])
acc = [cur]
for i in range(2, N - M + 1):
    cur -= A[i - 1]
    cur += A[i + M - 2]
    acc.append(cur)

cur = sum((idx + 1) * b for idx, b in enumerate(A[:M]))
ans = cur
for i in range(1, N - M + 1):
    cur -= A[i - 1]
    cur += A[i + M - 1] * M
    cur -= acc[i - 1]
    ans = max(ans, cur)
print(ans)
