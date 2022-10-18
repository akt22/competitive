from collections import defaultdict

N = int(input())
tree = defaultdict(set)

for _ in range(N - 1):
    a, b = list(map(int, input().split()))
    tree[a].add(b)
    tree[b].add(a)

for dep, dest in tree.items():
    if len(dest) == N - 1:
        print("Yes")
        exit()
print("No")
