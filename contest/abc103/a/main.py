from itertools import permutations

A = map(int, input().split())

ans = 10**9

for a1, a2, a3 in permutations(A):
    tmp = abs(a1 - a2)
    tmp += abs(a2 - a3)
    ans = min(ans, tmp)
print(ans)
