N = int(input())
A = list(map(int, input().split()))

n = max(A)
h = n // 2
r, r_origin = 0, 0
for a in A:
    if a == n:
        continue
    r_cand = n - a if a > h else a
    if r_cand >= r:
        r, r_origin = r_cand, a
print(n, r_origin)
