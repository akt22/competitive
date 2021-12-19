S = input()

base = 753

diff = 10**10
for i in range(len(S) - 2):
    diff = min(diff, abs(base - int(S[i:i + 3])))
print(diff)
