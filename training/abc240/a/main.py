a, b = list(map(int, input().split()))

if abs(a - b) == 1:
    print("Yes")
    exit()

a %= 10
b %= 10
if abs(a - b) == 1:
    print("Yes")
else:
    print("No")
