N = int(input())

l = [list(map(int, input().split())) for _ in range(N)]
l.reverse()
ans = 0
for a, b in l:
    r = (ans + a) % b
    if r != 0:
        ans += b - r
print(ans)
