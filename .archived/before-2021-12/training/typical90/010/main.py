from itertools import accumulate

N = int(input())

c1, c2 = [], []
for _ in range(N):
    c, p = list(map(int, input().split()))
    if c == 1:
        c1.append(p)
        c2.append(0)
    else:
        c2.append(p)
        c1.append(0)

sum_1 = list(accumulate(c1))
sum_1.insert(0, 0)
sum_2 = list(accumulate(c2))
sum_2.insert(0, 0)

Q = int(input())

for _ in range(Q):
    l, r = list(map(int, input().split()))
    p1 = sum_1[r] - sum_1[l - 1]
    p2 = sum_2[r] - sum_2[l - 1]
    print(p1, p2)
