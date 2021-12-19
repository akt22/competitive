from bisect import insort_right

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

A.sort()

for i in range(M):
    m = A.pop(-1)
    m //= 2
    insort_right(A, m)
print(sum(A))
