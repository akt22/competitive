# from bisect import bisect

N, X = list(map(int, input().split()))
A = list(map(int, input().split()))

# print(bisect(A, X))

l, r = 0, N
while l < r:
    m = (l + r) // 2
    if A[m] == X:
        print(m + 1)
        exit()
    elif A[m] < X:
        l = m + 1
    else:
        r = m
