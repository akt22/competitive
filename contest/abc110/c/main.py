S = input()
T = input()

d = {}

for idx, s in enumerate(S):
    if s in d:
        if d[s] == T[idx]:
            continue
        else:
            print("No")
            exit()
    d[s] = T[idx]

d = {}
for idx, s in enumerate(T):
    if s in d:
        if d[s] == S[idx]:
            continue
        else:
            print("No")
            exit()
    d[s] = S[idx]
print("Yes")
