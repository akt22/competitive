N, X, Y, Z = list(map(int, input().split()))
A = []
for i, x in zip(range(1, N + 1), map(int, input().split())):
    A.append([i, x])
B = []
for i, x in zip(range(1, N + 1), map(int, input().split())):
    B.append([i, x])
S = [[i + 1, a[1] + b[1]] for i, (a, b) in enumerate(zip(A, B))]

ans = set()

A.sort(key=lambda x: [x[1], -x[0]], reverse=True)
B.sort(key=lambda x: [x[1], -x[0]], reverse=True)
S.sort(key=lambda x: [x[1], -x[0]], reverse=True)

for i in range(X):
    ans.add(A[i][0])

b = 0
for i, score in B:
    if i in ans:
        continue
    if b == Y:
        break
    ans.add(i)
    b += 1

s = 0
for i, score in S:
    if i in ans:
        continue
    if s == Z:
        break
    ans.add(i)
    s += 1

print(*sorted(ans), sep="\n")
