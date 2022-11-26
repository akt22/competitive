N, M, B = list(map(int, input().split()))
A = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = B * N * M
for a in A:
    ans += a * M
for c in C:
    ans += c * N
print(ans)
