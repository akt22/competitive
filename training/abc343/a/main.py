A, B = list(map(int, input().split()))

if A + B > 9:
    print(9)
elif A + B < 1:
    print(A + B + 1)
else:
    print(A + B - 1)
