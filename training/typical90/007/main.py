import bisect

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = [int(input()) for _ in range(Q)]

A.sort()
for b in B:
    l = bisect.bisect_left(A, b)
    if l == 0:
        print(abs(b - A[l]))
    elif l == N:
        print(abs(b - A[l - 1]))
    else:
        print(min(abs(b - A[l]), abs(b - A[l - 1])))
