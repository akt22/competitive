N = int(input())
A = list(map(int, input().split()))

ans = 0
for a in A:
    ans += a - 10 if a > 10 else 0
print(ans)
