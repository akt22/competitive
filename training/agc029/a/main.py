S = input()

r_s = S[::-1]
lb = len(S) - 1
for s in r_s:
    if s == "B":
        lb -= 1
    else:
        break

ans = 0
for idx, s in enumerate(S):
    if s == "B":
        if lb - idx < 0 or lb < 0:
            break
        ans += lb - idx
        lb -= 1
        while S[lb] == "B":
            lb -= 1
print(ans)
