N = int(input())
A = list(map(int, input().split()))

(fv, fi), (sv, si) = ((A[0], 0), (A[1], 1)) if A[0] > A[1] else ((A[1], 1), (A[0], 0))

if N == 2:
    print(si + 1)
    exit()

for i in range(2, N):
    a = A[i]
    if sv > a:
        continue
    if fv < a:
        sv = fv
        si = fi
        fv = a
        fi = i
    else:
        sv = a
        si = i
print(si + 1)
