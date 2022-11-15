S = input()

ans = ""
for c in S:
    if c == "6":
        c = "9"
    elif c == "9":
        c = "6"
    ans += c
print(ans[::-1])
