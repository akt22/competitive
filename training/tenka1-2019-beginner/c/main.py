N = int(input())
S = list(input())

ans = [N] * (N + 1)
ans[0] = S.count(".")
for i in range(1, N + 1):
    if S[i - 1] == ".":
        ans[i] = ans[i - 1] - 1
    else:
        ans[i] = ans[i - 1] + 1
print(min(ans))
