from math import sqrt

N = int(input())


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if i != 2 and i % 2 == 0:
            continue
        if n % i == 0:
            return False
    return True


print("YES") if is_prime(N) else print("NO")
