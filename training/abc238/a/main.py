n = int(input())

if n >= 5:
    print("Yes")
    exit()

if 2**n > n**2:
    print("Yes")
else:
    print("No")
