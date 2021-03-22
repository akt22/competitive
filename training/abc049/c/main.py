S = input()

origin = set(["dream", "erase"])

i = len(S)
while i > 0:
    s = S[i - 5:i]
    if s in origin:
        i -= 5
        continue
    s = S[i - 6:i]
    if s in "eraser":
        i -= 6
        continue
    s = S[i - 7:i]
    if s in "dreamer":
        i -= 7
        continue
    print("NO")
    exit()
print("YES")
