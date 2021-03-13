N = input()

base = 10**3
m = []
for i in range(1, 6):
    m.append(i * ((base ** (i + 1) - 1) - (base ** i) + 1))


l = len(N)
N = int(N)

if l <= 3:
    print(0)
    exit()

r = range(l // 3 - 1) if l % 3 != 0 else range(l // 3 - 2)

ans = 0
for i in r:
    ans += m[i]

if l % 3 != 0:
    b = l - (l % 3)
    a = l // 3
else:
    b = (l // 3 - 1) * 3
    a = l // 3 - 1
start = 10 ** b
ans += (N - start + 1) * a
print(ans)
