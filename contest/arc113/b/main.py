A, B, C = list(map(int, input().split()))

loop = {
    0: 1,
    1: 1,
    2: 4,
    3: 4,
    4: 2,
    5: 1,
    6: 1,
    7: 4,
    8: 4,
    9: 2
}

last = int(str(A)[-1])
if last in [0, 1, 5, 6]:
    print(last)
    exit()
c = pow(B, C, loop[last])
if c == 0:
    c = loop[last]
print(str(A**c)[-1])
