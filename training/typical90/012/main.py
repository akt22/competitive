H, W = list(map(int, input().split()))
Q = int(input())

queries = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(Q)]

mazes = [[False] * 2009 for _ in range(2009)]
moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]


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


u = UnionFind(H * W)
for i in range(Q):
    if queries[i][0] == 0:
        r, c = queries[i][1:]
        idx = r * W + c
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and mazes[nr][nc]:
                idx2 = nr * W + nc
                u.union(idx, idx2)
        mazes[r][c] = True
    else:
        ra, ca, rb, cb = queries[i][1:]
        idx = ra * W + ca
        idx2 = rb * W + cb
        if mazes[ra][ca] and mazes[rb][cb] and u.check(idx, idx2):
            print("Yes")
        else:
            print("No")
