S = input()

s_min = "z" * len(S)
s_max = "a" * len(S)

for i in range(len(S)):
    first = S[:i]
    second = S[i:]
    s = second + first
    s_min = min(s_min, s)
    s_max = max(s_max, s)
print(s_min)
print(s_max)
