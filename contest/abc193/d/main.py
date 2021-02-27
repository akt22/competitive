from collections import Counter


K = int(input())
S = input()[:-1]
T = input()[:-1]


def f(cnt):
    ret = 0
    for i in range(1, 10):
        if str(i) not in cnt:
            ret += i
        else:
            ret += i * (10**int(cnt[str(i)]))
    return ret


cnt = 0
for i in range(1, 10):
    s = Counter(S + str(i))
    for j in range(1, 10):
        t = Counter(T + str(j))
        c = s + t
        if any([v > K for v in c.values()]):
            continue
        if f(s) > f(t):
            print(i, j)
            cnt += 1
print(cnt)
