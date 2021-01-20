from math import gcd

N, X = map(int, input().split())
towns = list(map(int, input().split()))

towns.append(X)
towns.sort()

diff = [y - x for x, y in zip(towns, towns[1:])]

ans = diff[0]
if len(diff) != 1:
    for d in diff:
        ans = gcd(d, ans)
print(ans)
