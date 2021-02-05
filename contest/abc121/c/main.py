N, M = map(int, input().split())
shops = [list(map(int, input().split())) for _ in range(N)]

shops.sort(key=lambda x: x[0])

ans = 0
cnt = 0
for a, b in shops:
    if M - cnt >= b:
        ans += (a * b)
        cnt += b
    else:
        ans += (M - cnt) * a
        break
print(ans)
