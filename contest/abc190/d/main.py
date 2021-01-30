from math import sqrt
N = int(input())

pre = 2 * N

ans = 0
for n in range(1, int(sqrt(2 * N)) + 1):
    if (pre - n * (n - 1)) % (2 * n) == 0:
        ans += 1
print(ans * 2)
