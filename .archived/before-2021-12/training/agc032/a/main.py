N = int(input())
B = list(map(lambda x: int(x) - 1, input().split()))

ans = []

INF = 10**9
while B:
    eraseable = (0, -INF)
    for i in range(len(B)):
        if i == B[i] and eraseable[1] < B[i]:
            eraseable = (i, B[i])

    if eraseable[1] == -INF:
        print(-1)
        exit()

    ans.append(B.pop(eraseable[0]) + 1)
print(*reversed(ans), sep="\n")
