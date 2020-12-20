H, W = map(int, input().split())
sx, sy = map(lambda x: int(x) - 1, input().split())
gx, gy = map(lambda x: int(x) - 1, input().split())
board = []
for _ in range(H):
    board.append(list(map(int, input().split())))


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


uf = UnionFind(H * W)
edges = []
ans = 0
for i in range(H):
    for j in range(W):
        ans += board[i][j]
        for (dx, dy) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = i + dx, j + dy
            if 0 <= nx < H and 0 <= ny < W:
                edges.append((i * W + j, nx * W + ny, - board[i][j] * board[nx][ny]))

for u, v, cost in sorted(edges, key=lambda x: x[2]):
    if not uf.check(u, v):
        uf.union(u, v)
        ans -= cost
print(ans)
