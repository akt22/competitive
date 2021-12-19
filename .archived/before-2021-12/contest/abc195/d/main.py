N, M, Q = list(map(int, input().split()))
bagages = [list(map(int, input().split())) for _ in range(N)]
caps = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(Q)]

bagages.sort(key=lambda x: x[1], reverse=True)

# どの箱にどの荷物を入れることができるかを保存するリスト（価値の降順に保存される）
a = [[] for _ in range(M)]

for idx, cap in enumerate(caps):
    for i, (w, v) in enumerate(bagages):
        if cap >= w:
            a[idx].append((i, v))

# 容量が小さい順番に見ていきたいので順番を保存
c = sorted(list(zip(range(0, M), caps)), key=lambda x: x[1])

for l, r in queries:
    choice = set()
    ans = 0
    # 容量が小さい順に見ていく
    for i, _ in c:
        if l - 1 <= i <= r - 1:
            continue
        box = a[i]
        # 箱には価値の降順で保存されているので、1つずつ見ていく
        for idx, v in box:
            if idx in choice:
                continue
            ans += v
            choice.add(idx)
            break
    print(ans)
