S = input()

alphabet = set([chr(i) for i in range(97, 123)])
uniq = set(S)

if len(S) < 26:
    for a in range(97, 123):
        a = chr(a)
        if a not in uniq:
            print(S + a)
            exit()

S = [ord(a) for a in S]

for i in range(len(S) - 1, 0, -1):
    if S[i - 1] <= S[i]:
        ans = [s for s in S[:i - 1]]
        uniq = set(ans)
        for a in range(S[i - 1] + 1, 123):
            if a not in uniq:
                ans.append(a)
                print(*[chr(a) for a in ans], sep="")
                exit()
print(-1)
