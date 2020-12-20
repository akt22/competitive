N, Q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(Q)]


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]

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


u = UnionFind(N)

for p, a, b in queries:
    if p == 0:
        u.union(a, b)
    else:
        if u.check(a, b):
            print("Yes")
        else:
            print("No")
