N = int(input())
exist = False

for i in range(N):
    ans = []
    A = list(map(int, input().split()))
    for j, a in enumerate(A):
        if a != 0:
            ans.append(j + 1)
    if ans:
        print(*ans)
        exist = True

if not exist:
    print()
