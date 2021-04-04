from collections import defaultdict
N, M = list(map(int, input().split()))
problems = [input().split() for _ in range(M)]

d = defaultdict(int)
ac = {}
for p, s in problems:
    p = int(p)
    if p in ac:
        continue
    if s == "AC":
        ac[p] = d[p]
    else:
        d[p] += 1

total_wa = 0
for p in ac:
    total_wa += d[p]
print(len(ac), total_wa)
