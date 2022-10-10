S1 = input()
S2 = input()

ans = True
if S1[0] == "#" and S2[1] == "#":
    ans = False if S1[1] == "." and S2[0] == "." else True
if S1[1] == "#" and S2[0] == "#":
    ans = False if S1[0] == "." and S2[1] == "." else True
print("Yes" if ans else "No")
