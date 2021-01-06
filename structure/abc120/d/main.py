N, M = map(int, input().split())
edges = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [-1] * n

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.par[x] > self.par[y]:
            x, y = y, x
        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self, x):
        return -self.par[self.find(x)]

    def check(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.par) if x < 0]

    def group_count(self):
        return len(self.roots())


u = UnionFind(N)
ans = [0] * M
d = N * (N - 1) // 2
ans[-1] = d

for i in range(M - 1, 0, -1):
    a, b = edges[i]
    if u.check(a, b):
        ans[i - 1] = d
    else:
        d -= u.size(a) * u.size(b)
        ans[i - 1] = d
        u.union(a, b)

print(*ans, sep="\n")
