from math import ceil

A, B, C, D = list(map(float, input().split()))

if D * C - B <= 0:
    print("-1")
    exit()

print(ceil(A / (D * C - B)))
