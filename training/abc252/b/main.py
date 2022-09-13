N, K = list(map(int, input().split()))

A = list(map(int, input().split()))

B = set()
for i in list(map(int, input().split())):
    B.add(i)

ma = max(A)
f = set()
for i, a in enumerate(A):
    if a == ma:
        f.add(i + 1)

print("No" if len(f & B) == 0 else "Yes")
