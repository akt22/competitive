from collections import Counter

n = int(input())
v = list(map(int, input().split()))

a = Counter(v[::2]).most_common(2) + [(0, 0)]
b = Counter(v[1::2]).most_common(2) + [(0, 0)]

if a[0][0] != b[0][0]:
    print(n - a[0][1] - b[0][1])
else:
    print(n - max(a[0][1] + b[1][1], a[1][1] + b[0][1]))
