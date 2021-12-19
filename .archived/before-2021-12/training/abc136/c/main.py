N = int(input())
H = list(map(int, input().split()))

ma = 0
for i in range(N - 1):
    d = H[i + 1] - H[i]
    if d < 0:
        ma = max(H[i] - 1, ma)
    # print(f"{ma} {H[i + 1]}")
    if ma - H[i + 1] > 0:
        print("No")
        exit()

print("Yes")
