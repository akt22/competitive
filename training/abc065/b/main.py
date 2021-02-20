N = int(input())

A = [int(input()) - 1 for _ in range(N)]

ans = 1
lighted = 0
while ans <= N:
    lighted = A[lighted]
    if lighted == 1:
        print(ans)
        exit()
    ans += 1
print(-1)
