from math import ceil

A, B = list(map(int, input().split()))

if A == B:
    print(1)
    exit()

print(ceil((B - A) / (A - 1.)) + 1)
