N = input()[::-1]

for i in range(len(N)):
    if N[i] != "0":
        if N[i:] == N[i:][::-1]:
            print("Yes")
            exit()
        else:
            print("No")
            exit()
print("Yes")
