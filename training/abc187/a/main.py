A, B = input().split()

sa, sb = 0, 0
for a, b in zip(A, B):
    sa += int(a)
    sb += int(b)
print(max(sa, sb))
