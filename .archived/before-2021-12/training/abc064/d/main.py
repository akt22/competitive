N = int(input())
S = input()

cnt = 0
pre = ""
for s in S:
    if s == "(":
        cnt += 1
    else:
        cnt -= 1
        if cnt < 0:
            pre += "("
            cnt += 1
print(pre + S + ")" * cnt)
