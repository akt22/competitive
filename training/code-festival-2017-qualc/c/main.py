
s = input()
n = len(s)
l = 0
r = n - 1
ans = 0
while l < r:
    if s[l] == s[r]:
        l += 1
        r -= 1
    elif s[l] == 'x':
        l += 1
        ans += 1
    elif s[r] == 'x':
        r -= 1
        ans += 1
    else:
        ans = -1
        break
print(ans)
