N = input()

INF = 1 << 60
ans = INF
for i in range(2**len(N)):
    tmp = 0
    cnt = 0
    for j in range(len(N)):
        if (i >> j) & 1:
            tmp += int(N[j])
            cnt += 1
    if tmp % 3 == 0 and tmp != 0:
        ans = min(ans, len(N) - cnt)
print(ans) if ans != INF else print(-1)
