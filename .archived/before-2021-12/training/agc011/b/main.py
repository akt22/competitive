N = int(input())
A = list(map(int, input().split()))

A.sort()
sums = 0
t = 0
for i, a in enumerate(A):
    if 2 * sums < a:
        t = i
    sums += a
print(N - t)
