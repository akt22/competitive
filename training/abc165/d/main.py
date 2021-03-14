from math import floor

A, B, N = list(map(int, input().split()))

x = B - 1 if N >= B else N
ans = floor(A / B * x) - floor(x / B)
print(ans)
