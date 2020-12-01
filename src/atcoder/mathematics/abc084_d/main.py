Q = int(input())
queries = [list(map(int, input().split())) for _ in range(Q)]


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if i != 2 and i % 2 == 0:
            continue
        if n % i == 0:
            return False
    return True


d = {0: 0}
for i in range(3, 10**5 + 1, 2):
    if is_prime(i) and is_prime((i + 1) // 2):
        d[i] = 1

for i in range(3, 10**5 + 1):
    d[i] = d.get(i, 0) + d.get(i - 1, 0)

for l, r in queries:
    print(d[r] - d.get(l - 1, 0))
