N = int(input())

if N % 2 != 0:
    print()
    exit()


def check(s):
    l, r = 0, 0
    for c in s:
        if c == "(":
            l += 1
        else:
            r += 1
        if l < r:
            return False
    return True if l == r else False


ans = []
for i in range(2**N):
    s = ""
    for j in range(N):
        s += ")" if (i >> j) & 1 else "("
    if check(s):
        ans.append(s)
print(*sorted(ans), sep="\n")
