from bisect import bisect_left

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

first = A[:N // 2]
second = A[N // 2:]

P = []
for i in range(2**len(first)):
    tmp = 0
    for j in range(len(first)):
        if (i >> j) & 1:
            tmp += first[j]
    P.append(tmp)

Q = []
for i in range(2**len(second)):
    tmp = 0
    for j in range(len(second)):
        if (i >> j) & 1:
            tmp += second[j]
    Q.append(tmp)
Q.sort()

for p in P:
    k = K - p
    pos = bisect_left(Q, k)
    if pos < len(Q) and Q[pos] == k:
        print("Yes")
        exit()
print("No")
