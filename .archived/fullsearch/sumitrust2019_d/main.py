N = int(input())
S = input()


def check(v):
    flg1 = False
    flg2 = False
    flg3 = False
    for s in S:
        if v[0] == s and not flg1 and not flg2:
            flg1 = True
            continue
        if v[1] == s and flg1 and not flg2:
            flg2 = True
            continue
        if v[2] == s and flg1 and flg2:
            flg3 = True

    return flg1 and flg2 and flg3


ans = set()
for i in range(0, 1000):
    v = str(i).zfill(3)
    if check(v):
        ans.add(v)
print(len(ans))
