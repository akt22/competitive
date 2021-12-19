N = int(input())
A = list(map(int, input().split()))


for i in range(N - 1, -1, -1):
    tmp = A[i]
    for j in range(2 * (i + 1), N + 1, i + 1):
        tmp ^= A[j - 1]
    A[i] = tmp

ans = 0
anss = []
for i, v in enumerate(A):
    i += 1
    if v == 1:
        ans += 1
        anss.append(i)
print(ans)
if ans != 0:
    print(*anss)
