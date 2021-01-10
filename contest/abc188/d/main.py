N, C = map(int, input().split())

events = []
for i in range(N):
    a, b, c = map(int, input().split())
    a -= 1
    events.append([a, c])
    events.append([b, -c])

events.sort()
ans, fee, t = 0, 0, 0
for x, y in events:
    if x != t:
        ans += min(C, fee) * (x - t)
        t = x
    fee += y
print(ans)
