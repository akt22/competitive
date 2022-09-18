from itertools import accumulate

N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
questions = [list(map(int, input().split())) for _ in range(Q)]

acc = list(accumulate(A, initial=0))
for l, r in questions:
    print(acc[r] - acc[l - 1])
