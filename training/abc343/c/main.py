N = int(input())

ans = 1
for i in range(1, N + 1):
    k = i**3
    if k > N:
        break
    v = str(k)
    if v == v[::-1]:
        ans = k
print(ans)
