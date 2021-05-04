N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort(key=lambda x: 2 * x[0] + x[1], reverse=True)

a = 0
for i in range(N):
    a += AB[i][0]

b = 0
for i, (_a, _b) in enumerate(AB):
    b += _a + _b
    a -= _a
    if b > a:
        print(i + 1)
        exit()
