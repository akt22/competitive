N = int(input())

S = [input() for _ in range(N)]


ans = 1
for idx, s in enumerate(S):
    if s == "OR":
        ans += 2**(idx + 1)
print(ans)
