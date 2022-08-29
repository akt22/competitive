X, Y, N = list(map(int, input().split()))

ans = 0
ans += Y * (N // 3)
if N % 3 == 1:
    ans += X
elif N % 3 == 2:
    ans += X * 2
print(min(ans, X * N))
