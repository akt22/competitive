N = int(input())


def sn(n, a, d):
    return n * (2 * a + (n - 1) * d) // 2


ans = 0
for i in range(1, N + 1):
    for j in range(i, N + 1, i):
        ans += j
    # ans += sn(N // i, i, i)
print(ans)
