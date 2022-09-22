N = int(input())
A = list(map(int, input().split()))

a = sorted(list(set(A)))
rank = {}
for i, _a in enumerate(a):
    rank[_a] = i + 1

print(*[rank[a] for a in A], sep=" ")
