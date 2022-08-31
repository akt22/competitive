N = int(input())
P = list(map(int, input().split()))

ans = 0
i = N - 2
while i >= 0:
    p = P[i]
    i = p - 2
    ans += 1
print(ans)
