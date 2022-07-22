S = input()

tmp = 0

for s in S:
    if tmp == 0 and (s == "i" or s == "I"):
        tmp += 1
    elif tmp == 1 and (s == "c" or s == "C"):
        tmp += 1
    elif tmp == 2 and (s == "t" or s == "T"):
        tmp += 1
    elif tmp >= 3:
        break
print("YES" if tmp == 3 else "NO")
