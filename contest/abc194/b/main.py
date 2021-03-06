N = int(input())

A = []
B = []
for idx in range(N):
    a, b = list(map(int, input().split()))
    A.append([idx, a])
    B.append([idx, b])
A.sort(key=lambda x: x[1])
B.sort(key=lambda x: x[1])

if A[0][0] != B[0][0]:
    print(max(A[0][1], B[0][1]))
    exit()

ans1 = A[0][1] + B[0][1]
ans2 = max(A[0][1], B[1][1])
ans3 = max(A[1][1], B[0][1])
print(min(ans1, ans2, ans3))
