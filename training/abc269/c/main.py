from itertools import product

S = int(input())

on = []
for i in range(61):
    if S & (1 << i):
        on.append(i)

ans = []
comb = list(product(range(2), repeat=len(on)))
for it in comb:
    tmp = 0
    for i, v in enumerate(it):
        if v:
            tmp += 1 << on[i]
    ans.append(tmp)

print(*sorted(ans), sep="\n")
