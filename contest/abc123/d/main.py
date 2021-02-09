X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

l = []
for i, a in enumerate(A[:K]):
    for j, b in enumerate(B[:K]):
        l.append(a + b)
l.sort(reverse=True)

l = l[:K]

ans = []
for e in l:
    for c in C:
        ans.append(e + c)
ans.sort(reverse=True)
print(*ans[:K], sep="\n")
