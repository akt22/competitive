S = list(input())
T = list(input())

diff = set()
for s, t in zip(S, T):
    if s < t:
        diff.add(ord(t) - ord(s))
    else:
        diff.add(26 - abs(ord(s) - ord(t)))
print("Yes") if len(diff) == 1 else print("No")
