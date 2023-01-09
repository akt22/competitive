from math import sqrt

Q = int(input())
queries = [int(input()) for _ in range(Q)]


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if i != 2 and i % 2 == 0:
            continue
        if n % i == 0:
            return False
    return True


for q in queries:
    print("Yes" if is_prime(q) else "No")
