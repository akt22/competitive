N = int(input())
A = [input() for _ in range(N)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

ans = ""

for i in range(N):
    for j in range(N):
        for _dx, _dy in zip(dx, dy):
            s = ""
            for k in range(N):
                x = (i + _dx * k) % N
                y = (j + _dy * k) % N
                s += A[x][y]
            ans = max(ans, s)
print(ans)
