N, M, T = list(map(int, input().split()))
A = list(map(int, input().split()))

bonus = [0] * N
for _ in range(M):
    x, y = list(map(int, input().split()))
    bonus[x - 1] = y

for i in range(N - 1):
    if T - A[i] <= 0:
        print("No")
        exit()
    T -= A[i]
    T += bonus[i + 1]
print("Yes")
