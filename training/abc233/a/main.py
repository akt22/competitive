X, Y = list(map(int, input().split()))
if Y - X > 0:
    m = 0 if (Y - X) % 10 == 0 else 1
    print((Y - X) // 10 + m)
else:
    print(0)
