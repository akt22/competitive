N = input()

n1, n2, n3 = N

if n1 == n2 and n2 == n3:
    print(N)
elif int(N) > int(n1 + n1 + n1):
    print(f"{int(n1)+1}{int(n1)+1}{int(n1)+1}")
else:
    print(f"{n1}{n1}{n1}")
