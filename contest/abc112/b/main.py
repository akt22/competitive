N, T = map(int, input().split())
path = [list(map(int, input().split())) for _ in range(N)]

ans = 10**9
for c, t in path:
    if T >= t:
        ans = min(ans, c)
if ans == 10**9:
    print("TLE")
else:
    print(ans)
