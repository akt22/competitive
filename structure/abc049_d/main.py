from collections import defaultdict

N, K, L = map(int, input().split())

roads = [map(int, input().split()) for _ in range(K)]
trains = [map(int, input().split()) for _ in range(L)]


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


uroad = UnionFind(N)
utrain = UnionFind(N)

for p, q in roads:
    uroad.union(p, q)
for r, s in trains:
    utrain.union(r, s)

m = defaultdict(int)
for i in range(1, N + 1):
    m[(uroad.root(i), utrain.root(i))] += 1

anss = []
for i in range(1, N + 1):
    ans = m[(uroad.root(i), utrain.root(i))]
    anss.append(str(ans))
print(" ".join(anss))
