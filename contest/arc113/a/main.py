K = int(input())

if K == 1:
    print(1)
    exit()

ans = 0
for a in range(1, K + 1):
    B = K // a
    if B == 0:
        continue
    elif B < a:
        continue
    for b in range(a, B):
        C = K // (a * b)
        if C == 0:
            continue
        elif C < a or C < b:
            continue
        tmp = set([a, b])
        if len(tmp) == 1:
            base = 3
            ans += 1
        else:
            base = 6
            ans += 3
        ans += base * (C - b)
print(ans)
