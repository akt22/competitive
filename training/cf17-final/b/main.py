from collections import Counter

S = input()
cnt = Counter(S)

if len(S) > 2 and len(cnt) != 3:
    print("NO")
    exit()

diff = 0
diff = max(diff, abs(cnt['a'] - cnt['b']))
diff = max(diff, abs(cnt['b'] - cnt['c']))
diff = max(diff, abs(cnt['c'] - cnt['a']))

if diff > 1:
    print("NO")
else:
    print("YES")
