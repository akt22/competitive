from collections import Counter

N = int(input())
S = input()

cnt = Counter(S)
MOD = 10**9 + 7

ans = 1
for ch in cnt.values():
    ans *= ch + 1
ans -= 1
print(ans % MOD)
