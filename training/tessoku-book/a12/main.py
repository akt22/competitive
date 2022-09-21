N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

l, r = 0, 10**9
while l < r:
    m = (l + r) // 2
    if sum([m // a for a in A]) < K:
        l = m + 1
    else:
        r = m
print(l)
