N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
ops = [list(map(int, input().split())) for _ in range(M)]

A.sort()
ops.sort(key=lambda x: x[1], reverse=True)

ans = 0
ops_idx = 0
for idx, a in enumerate(A):
    if len(ops) > ops_idx and a < ops[ops_idx][1]:
        ans += ops[ops_idx][1]
        ops[ops_idx][0] -= 1
        if ops[ops_idx][0] == 0:
            ops_idx += 1
    else:
        ans += a
print(ans)
