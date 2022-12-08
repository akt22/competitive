N, Q = list(map(int, input().split()))
L = [list(map(int, input().split())) for _ in range(N)]
queries = [list(map(int, input().split())) for _ in range(Q)]

for s, t in queries:
    print(L[s - 1][t])
