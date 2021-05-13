from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cand = list(range(N - 1, -1, -2))

cnt = Counter(A)

if set(cnt.keys()) != set(cand):
    print(0)
    exit()

MOD = 10**9 + 7
ans = 1
for k, v in cnt.items():
    if N % 2 == 1 and k == 0 and v != 1:
        print(0)
        exit()
    elif k != 0 and v != 2:
        print(0)
        exit()
    ans *= v
    ans %= MOD
print(ans)
