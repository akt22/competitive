N = int(input())
S = input()

ans = 0
for i in range(N):
    x, y = S[:i], S[i:]
    ans = max(ans, len(set(x) & set(y)))
print(ans)
