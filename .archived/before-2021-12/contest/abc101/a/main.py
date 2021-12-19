S = input()

ans = 0
for s in S:
    ans += 1 if s == "+" else -1
print(ans)
