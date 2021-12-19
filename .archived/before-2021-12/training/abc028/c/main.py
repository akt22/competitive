from itertools import combinations

A = list(map(int, input().split()))

ans = []
for s in combinations(A, 3):
    ans.append(sum(s))
ans.sort()
print(ans[-3])
