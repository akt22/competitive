Y = int(input())

y = Y - 2
m = y % 4
if m == 0:
    print(y + 2)
else:
    print(y + 6 - m)
