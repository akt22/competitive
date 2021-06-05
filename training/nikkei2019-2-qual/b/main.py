from collections import Counter

N = int(input())
D = list(map(int, input().split()))

MOD = 998244353

cnt = Counter(D)
ans = 1
if 0 not in cnt or cnt[0] > 1 or D[0] != 0:
    print(0)
    exit()
for i in range(len(cnt) - 1):
    if i not in cnt or i + 1 not in cnt:
        print(0)
        exit()
    ans *= pow(cnt[i], cnt[i + 1], MOD)
print(ans % MOD)
