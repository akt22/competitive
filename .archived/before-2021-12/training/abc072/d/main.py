N = int(input())
p = list(map(int, input().split()))

ans = 0
i = 1
while i <= N:
    if i == p[i - 1]:
        ans += 1
        i += 1
    i += 1
print(ans)
