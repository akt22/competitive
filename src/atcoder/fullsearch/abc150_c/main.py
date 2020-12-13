from itertools import permutations

N = int(input())

P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

a, b = 0, 0
for idx, p in enumerate(permutations(range(1, N + 1))):
    if p == P:
        a = idx
    if p == Q:
        b = idx

print(abs(a - b))
