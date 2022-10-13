N = int(input())
S = list(map(int, input().split()))


def f(a, b):
    return 4 * a * b + 3 * a + 3 * b


ans = 0
for s in S:
    passed = False
    for a in range(1, 500):
        if passed:
            break
        for b in range(1, 500):
            if f(a, b) == s:
                ans += 1
                passed = True
                break
            if f(a, b) > s:
                break
print(N - ans)
