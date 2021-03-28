N = int(input())

ans = 0

XA = 0
BA = 0
BX = 0
for _ in range(N):
    s = input()
    ans += s.count("AB")
    i = s[0] + s[-1]
    if i == "BA":
        BA += 1
    elif s[-1] == "A":
        XA += 1
    elif s[0] == "B":
        BX += 1

if BA:
    ans += BA - 1
    if XA:
        ans += 1
        XA -= 1
    if BX:
        ans += 1
        BX -= 1

ans += max(min(XA, BX), 0)
print(ans)
