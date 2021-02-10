S = input()

tmp = 0
for i in range(len(S)):
    if i % 2 == 0 and S[i] != "0":
        tmp += 1
    elif i % 2 == 1 and S[i] != "1":
        tmp += 1
ans = tmp

tmp = 0
for i in range(len(S)):
    if i % 2 != 0 and S[i] != "0":
        tmp += 1
    elif i % 2 != 1 and S[i] != "1":
        tmp += 1
print(min(ans, tmp))
