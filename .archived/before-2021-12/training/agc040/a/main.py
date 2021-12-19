S = input()
N = len(S) + 1

ans = 0
a = [0] * N

for i, s in enumerate(S):
    if s == "<":
        a[i + 1] = a[i] + 1

for i in range(len(S) - 1, -1, -1):
    if S[i] == ">":
        a[i] = max(a[i], a[i + 1] + 1)
print(sum(a))
