from math import sqrt

N = int(input())
M = 10 ** 9 + 7


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if i != 2 and i % 2 == 0:
            continue
        if n % i == 0:
            return False
    return True


d = {}
for i in range(2, N + 1):
    if is_prime(i):
        d[i] = 0
        for j in range(2, N + 1):
            tmp = j
            # tmp が i で割り切れるなら、まだ割る
            while tmp % i == 0 and tmp != 0:
                tmp /= i
                d[i] += 1

# x = p**n * q**m...ならば
# xの約数の数は (n+1)*(m+1)... で表せる
cnt = 1
for v in d.values():
    cnt *= v + 1
print(cnt % M)
