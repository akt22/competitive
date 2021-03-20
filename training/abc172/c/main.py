from itertools import accumulate

N, M, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = list(accumulate(A, initial=0))
b = list(accumulate(B, initial=0))

j = M
ans = 0
for i in range(N + 1):
    if a[i] > K:
        break
    while a[i] + b[j] > K:
        j -= 1
    ans = max(ans, i + j)

print(ans)
