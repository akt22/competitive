N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

end = 1

ans = 0

for start, a in enumerate(A):
    while end < N and A[end] - a <= K:
        end += 1
        ans += end - start - 1
print(ans)
