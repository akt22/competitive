from math import ceil

N, H = list(map(int, input().split()))
swing, throw = [], []
for i in range(N):
    a, b = list(map(int, input().split()))
    swing.append([i, a, b])
    throw.append([i, b])

swing.sort(key=lambda x: (x[1], -x[2]), reverse=True)
throw.sort(key=lambda x: x[1], reverse=True)

ans = 0
damage = 0
s_idx, a, b = swing[0]
for idx, b in throw:
    if a < b:
        damage += b
        ans += 1
        if damage >= H:
            print(ans)
            exit()
remain = H - damage
ans += ceil(remain / a)
print(ans)
