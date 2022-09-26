A, B, C, X = list(map(float, input().split()))

if X <= A:
    print(1.0)
elif X <= B:
    print(C / (B - A))
else:
    print(0.0)
