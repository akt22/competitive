S = input()

Y = int(S[-1])

if Y <= 2:
    print(S[:-2] + "-")
elif 3 <= Y <= 6:
    print(S[:-2])
else:
    print(S[:-2] + "+")
