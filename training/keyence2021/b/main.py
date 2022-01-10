from collections import Counter

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

ma = max(A)

counter = Counter(A)

ans = 0

for i in range(ma + 1):
    if i not in counter:
        ans += K * i
        print(ans)
        exit()
    if counter[i] < K:
        ans += i * (K - counter[i])
        K = counter[i]
if K > 0:
    ans += K * (ma + 1)
print(ans)
