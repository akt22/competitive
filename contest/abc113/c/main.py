N, M = map(int, input().split())

cities = [list(map(int, input().split())) for _ in range(M)]

memo = {}
cnt = [1] * (N + 1)
for p, y in sorted(cities, key=lambda x: x[1]):
    memo[y] = cnt[p]
    cnt[p] += 1

for p, y in cities:
    print(f"{p:0>6}{memo[y]:0>6}")
