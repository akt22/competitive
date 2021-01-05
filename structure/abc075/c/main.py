N, M = map(int, input().split())
edges = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]

    def root(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        self.par[x] = y

    def check(self, x, y):
        return self.root(x) == self.root(y)

    def roots(self):
        return set([self.root(node) for node in self.par])


cnt = 0

for i in range(M):
    u = UnionFind(N)
    for j, (a, b) in enumerate(edges):
        if i == j:
            continue
        u.union(a, b)
    # print(f"{i=}, {u.roots()}")
    if len(u.roots()) != 1:
        cnt += 1

print(cnt)
