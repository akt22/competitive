N = int(input())
A = list(map(int, input().split()))

now = 0
ans = 1
for i in range(1, N):
    l = A[i - 1]
    r = A[i]

    if now == 0:
        if l > r:
            now = -1
        elif l < r:
            now = 1
    elif now == 1:
        if l > r:
            ans += 1
            now = 0
    else:
        if l < r:
            ans += 1
            now = 0
print(ans)
