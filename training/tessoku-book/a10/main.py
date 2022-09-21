N = int(input())
A = list(map(int, input().split()))
D = int(input())
questions = [list(map(int, input().split())) for _ in range(D)]

lr = [0] * (N + 1)
rl = [0] * (N + 1)
for i in range(N):
    lr[i + 1] = max(A[i], lr[i])
    rl[i + 1] = max(A[N - i - 1], rl[i])

for l, r in questions:
    print(max(lr[l - 1], rl[N - r]))
