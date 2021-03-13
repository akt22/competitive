N, M, Q = list(map(int, input().split()))
bagages = [list(map(int, input().split())) for _ in range(N)]
caps = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(Q)]

bagages.sort(key=lambda x: x[1], reverse=True)

a = [[] for _ in range(M)]
for i, (w, v) in enumerate(bagages):
    for idx, cap in enumerate(caps):
        if cap >= w:
            a[idx].append((i, v))
print(a)

for l, r in queries:
    choice = set()
    ans = 0
    for i, box in enumerate(a):
        if l - 1 <= i <= r - 1:
            continue
        for idx, v in box:
            if idx in choice:
                continue
            ans += v
            choice.add(idx)
            break
    print(ans)
