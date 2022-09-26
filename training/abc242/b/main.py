from collections import Counter
from string import ascii_letters

S = input()
cnt = Counter(S)

print("".join(s * cnt.get(s, 0) for s in ascii_letters))
