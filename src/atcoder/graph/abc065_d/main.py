import sys
sys.setrecursionlimit(10**5)


N = int(input())

xs = []
ys = []
for i in range(N):
    x, y = map(int, input().split())
    xs.append((x, i))
    ys.append((y, i))

xs.sort()
ys.sort()


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

costs = []
for i in range(N - 1):
    x1, f = xs[i]
    x2, t = xs[i + 1]
    costs.append((x2 - x1, f, t))
    y1, f = ys[i]
    y2, t = ys[i + 1]
    costs.append((y2 - y1, f, t))

costs.sort()

res = 0
for cost, f, t in costs:
    if not u.check(f, t):
        res += cost
        u.union(f, t)

print(res)
