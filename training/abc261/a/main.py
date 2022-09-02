L1, R1, L2, R2 = list(map(int, input().split()))

if L1 <= L2 <= R1:
    print(min(R1 - L2, R2 - L2))
elif L2 <= L1 <= R2:
    print(min(R2 - L1, R1 - L1))
else:
    print(0)
