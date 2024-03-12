N = int(input())
A = list(map(int, input().split()))
cur = [list(map(int, input().split())) for _ in range(N - 1)]

for i in range(N - 1):
    a = A[i]
    coef = a // cur[i][0]
    A[i + 1] += coef * cur[i][1]

print(A[-1])
