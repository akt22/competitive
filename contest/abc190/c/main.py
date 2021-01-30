N, M = map(int, input().split())
conditions = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
dishes = [list(map(int, input().split())) for _ in range(K)]

ans = 0
for i in range(2**K):
    balls = set()
    cnt = 0
    for j in range(K):
        if (i >> j) & 1:
            balls.add(dishes[j][0])
        else:
            balls.add(dishes[j][1])
    for a, b in conditions:
        if a in balls and b in balls:
            cnt += 1
    ans = max(ans, cnt)
print(ans)
