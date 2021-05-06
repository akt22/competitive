from math import sqrt

N = int(input())


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if i != 2 and i % 2 == 0:
            continue
        if n % i == 0:
            return False
    return True


# cnt = 0
# for i in range(2, N):
#     if is_prime(i):
#         cnt += 1
# print(cnt)


# =====

A = range(2, N)

for p in range(2, int(sqrt(N)) + 1):
    tmp = []
    for a in A:
        if a == p or a % p != 0:
            tmp.append(a)
    A = tmp
print(len(A))
