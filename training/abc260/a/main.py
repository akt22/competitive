S = input()

if S[0] != S[1] and S[0] != S[2]:
    print(S[0])
    exit()
if S[1] != S[0] and S[1] != S[2]:
    print(S[1])
    exit()
if S[2] != S[0] and S[2] != S[1]:
    print(S[2])
    exit()
print(-1)
