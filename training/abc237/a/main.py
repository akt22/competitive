
N = int(input())

upper = 2**31
lower = -2**31

if lower <= N < upper:
    print("Yes")
else:
    print("No")
