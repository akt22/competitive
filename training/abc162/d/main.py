from collections import Counter

N = int(input())
S = input()

correct = set(["R", "G", "B"])
c = Counter(S)

if len(c.keys()) < 3:
    print(0)
    exit()

ans = 1
for v in c.values():
    ans *= v

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        k = 2 * j - i
        if k < 0 or k >= N:
            continue
        if set([S[i], S[j], S[k]]) == correct:
            ans -= 1
print(ans)
