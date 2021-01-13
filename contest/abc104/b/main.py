S = input()

l = len(S)

a, c, upper = 100, 100, 0
for idx, s in enumerate(S):
    upper += 1 if s.isupper() else 0
    if s == "A":
        a = idx
    elif s == "C":
        c = idx

if a == 0 and 2 <= c <= (l - 2) and upper == 2:
    print("AC")
else:
    print("WA")
