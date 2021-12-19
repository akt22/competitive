from functools import reduce


N = int(input())
A = list(map(int, input().split()))

INF = 1 << 60
ans = INF

for i in range(0, 2**N, 2):
    sections = []
    prev = 0
    for j in range(N):
        if (i >> j) & 1 and A[prev:j]:
            sections.append(A[prev:j])
            prev = j
    sections.append(A[prev:])
    ans = min(ans, reduce(lambda a, b: a ^ b, [reduce(lambda x, y: x | y, sec) for sec in sections]))
print(ans)
