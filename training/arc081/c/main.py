from collections import Counter

N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)

a, b = 0, 0
for k, v in cnt.items():
    if v >= 4:
        if k >= a:
            a = k
            b = k
        elif k >= b:
            b = k
    elif v >= 2:
        if k >= a:
            b = a
            a = k
        elif k >= b:
            b = k
print(a * b)
