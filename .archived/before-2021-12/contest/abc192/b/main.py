S = input()

for idx, s in enumerate(S):
    if (idx + 1) % 2 == 0:
        if s.isupper():
            continue
        else:
            print("No")
            exit()

    else:
        if s.islower():
            continue
        else:
            print("No")
            exit()
print("Yes")
