A, B, C = sorted(list(map(int, input().split())))

s = A + B + C

if (s - C) % 2 == 0:
    print((3 * C - s) // 2)
else:
    print((3 * (C + 1) - s) // 2)
