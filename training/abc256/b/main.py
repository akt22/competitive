from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))

A.reverse()
a = list(accumulate(A))

print(sum([1 for _a in a if _a >= 4]))
