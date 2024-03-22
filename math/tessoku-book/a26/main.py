from math import sqrt

Q = int(input())
X = [int(input()) for _ in range(Q)]

N = 300000
deleted = [False] * 300009

# O(N * sqrt(X))
# def is_prime(n):
#     for i in range(2, int(sqrt(n)) + 1):
#         if i != 2 and i % 2 == 0:
#             continue
#         if n % i == 0:
#             return False
#     return True

# O(N loglog N)
for i in range(2, int(sqrt(N)) + 1):
    if deleted[i]:
        continue
    for j in range(i * 2, N + 1, i):
        deleted[j] = True

for x in X:
    print("Yes" if not deleted[x] else "No")
