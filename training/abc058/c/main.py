from collections import Counter

n = int(input())
S = [input() for _ in range(n)]

cnt = {}
chars = set([chr(i) for i in range(97, 97 + 26)])
for s in S:
    counter = Counter(s)
    chars = chars.intersection(counter.keys())
    for k, v in counter.items():
        if k in cnt:
            cnt[k] = min(cnt[k], v)
        else:
            cnt[k] = v

ans = ""
for ch in sorted(chars):
    ans += ch * cnt[ch]
print(ans)
