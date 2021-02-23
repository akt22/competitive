from collections import defaultdict

S = input()
S = S[::-1]

ans, seq = 0, 0
prev = ""
d = defaultdict(int)
for idx, s in enumerate(S):
    if prev == s:
        seq += 1
    else:
        if seq >= 2:
            ans += (idx - seq) - (d[prev] - seq)
            d = defaultdict(int)
            d[prev] = idx
        seq = 1
    d[s] += 1
    prev = s

idx = len(S)
if seq >= 2:
    ans += (idx - seq) - (d[s] - seq)
print(ans)
