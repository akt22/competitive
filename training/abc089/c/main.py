from itertools import combinations
N = int(input())
names = [input() for _ in range(N)]


initials = {
    "M": 0,
    "A": 0,
    "R": 0,
    "C": 0,
    "H": 0
}
for name in names:
    if name[0] in initials:
        initials[name[0]] += 1

ans = 0
for a, b, c in combinations(initials, 3):
    ans += initials[a] * initials[b] * initials[c]
print(ans)
