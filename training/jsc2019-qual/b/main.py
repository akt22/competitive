N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

MOD = 10**9 + 7

n = 0
for i in range(N):
    for j in range(i + 1, N):
        if A[i] > A[j]:
            n += 1
x = K * (K + 1) * n // 2

n = 0
for i in range(N):
    for j in range(0, i):
        if A[i] > A[j]:
            n += 1
y = K * (K - 1) * n // 2
print((x + y) % MOD)
