from collections import Counter

K = int(input())
S = input()[:-1]
T = input()[:-1]

deck = Counter(dict(zip([str(i) for i in range(1, 10)], [K] * 10)))
deck -= Counter(S)
deck -= Counter(T)


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
    i = str(i)
    s = Counter(S + i)
    for j in range(1, 10):
        j = str(j)
        t = Counter(T + j)
        c = s + t
        if any([v > K for v in c.values()]):
            continue
        if f(s) > f(t):
            if i == j:
                cnt += deck[i] * (deck[i] - 1)
            else:
                cnt += deck[i] * deck[j]

total = sum(deck.values())
print(float(cnt) / (total * (total - 1)))
