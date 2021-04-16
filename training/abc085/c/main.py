N, Y = list(map(int, input().split()))

for i in range(N + 1):
    for j in range(N + 1):
        k = N - (i + j)
        if k < 0:
            continue
        if 10000 * i + 5000 * j + 1000 * k == Y:
            print(i, j, k)
            exit()
print(-1, -1, -1)
