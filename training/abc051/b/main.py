K, S = list(map(int, input().split()))

ans = 0
for x in range(K + 1):
    for y in range(x, K + 1):
        z = S - (x + y)
        if z < 0 or z > K or x > z or y > z:
            continue
        s = len(set([x, y, z]))
        if s == 1:
            ans += 1
        elif s == 2:
            ans += 3
        else:
            ans += 6
print(ans)
