N, M = map(int, input().split())

switches = [list(map(lambda x: int(x) - 1, input().split()))[1:] for _ in range(M)]
conditions = list(map(int, input().split()))

cnt = 0
for i in range(2**N):
    on = []
    flg = True
    for j in range(N):
        if (i >> j) & 1:
            on.append(j)
    for idx, switch in enumerate(switches):
        mod = len(set(on) & set(switch)) % 2
        if mod != conditions[idx]:
            flg = False
    if flg:
        cnt += 1
print(cnt)
