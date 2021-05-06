from itertools import accumulate

N, Q = map(int, input().split())

distances = list(map(int, input().split()))

routes = list(map(int, input().split()))

M = 10**9 + 7

_cost = [0]
for i in range(N - 1):
    d = pow(distances[i], distances[i + 1], M)
    _cost.append(d)
cost = list(accumulate(_cost))

routes.insert(0, 1)
routes.append(1)
ans = 0
for i in range(Q + 1):
    ans += abs(cost[routes[i + 1] - 1] - cost[routes[i] - 1]) % M
print(ans % M)
