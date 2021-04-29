S = input()
N = len(S)

ans = 0
for i, s in enumerate(S):
    if i == 0 or i == N - 1:
        ans += N - 1
    else:
        up, down = (1, 2) if s == "U" else (2, 1)
        ans += up * (N - i - 1)
        ans += down * i
print(ans)
