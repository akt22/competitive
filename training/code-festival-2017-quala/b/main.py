N, M, K = list(map(int, input().split()))

for i in range(M + 1):
    for j in range(N + 1):
        b = (N - j) * i + (M - i) * j
        if b == K:
            print("Yes")
            exit()
print("No")
