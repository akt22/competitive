from itertools import accumulate

N = int(input())
S = input()

lr, rl = [], []
for s in S:
    if s == "W":
        lr.append(1)
        rl.append(0)
    else:
        lr.append(0)
        rl.append(1)
a_lr = list(accumulate(lr))
a_rl = list(accumulate(reversed(rl)))

ans = 1 << 60
for l, r in zip(a_lr, reversed(a_rl)):
    if ans > l + r - 1:
        ans = l + r - 1
print(ans)
