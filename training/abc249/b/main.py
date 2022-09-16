import string

from collections import Counter

upper = set(string.ascii_uppercase)
lower = set(string.ascii_lowercase)

S = input()
s = Counter(S)

u = 0
l = 0
for c, cnt in s.items():
    if cnt > 1:
        print("No")
        exit()
    u += 1 if c in upper else 0
    l += 1 if c in lower else 0

print("Yes" if u != 0 and l != 0 else "No")
