N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

INF = 1 << 60
argmin = INF
min_value = INF
for i, t in enumerate(T):
    if t < min_value:
        min_value = t
        argmin = i

time = INF
ans = [0] * N
for i in range(N):
    idx = (argmin + i) % N
    time = min(time, T[idx])
    ans[idx] = time
    time += S[idx]
print(*ans, sep='\n')
