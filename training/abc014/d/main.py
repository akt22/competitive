from collections import defaultdict, deque

N = int(input())
g = defaultdict(list)
for _ in range(N - 1):
    x, y = list(map(lambda x: int(x) - 1, input().split()))
    g[x].append(y)
    g[y].append(x)

Q = int(input())
edges = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(Q)]


class LowestCommonAncestor:
    def __init__(self, edges):
        self.n = len(edges)
        self.edges = edges

        self.depths, self.parents = self._dfs()
        self.dbl = self._doubling()

    def _dfs(self):
        depths = [-1] * self.n
        parents = [-1] * self.n
        depths[0] = 0
        q = deque([0])
        while q:
            a = q.pop()
            for b in self.edges[a]:
                if depths[b] + 1:
                    continue
                parents[b] = a
                depths[b] = depths[a] + 1
                q.append(b)
        return depths, parents

    def _doubling(self):
        dbl = [self.parents]
        for _ in range(max(self.depths).bit_length() - 1):
            parents = dbl[-1]
            new_parents = [-1] * self.n
            for i in range(self.n):
                if parents[i] + 1:
                    new_parents[i] = parents[parents[i]]
            dbl.append(new_parents)
        return dbl

    def lca(self, a, b):
        if self.depths[a] < self.depths[b]:
            a, b = b, a
        for i in range((self.depths[a] - self.depths[b]).bit_length()):
            if self.depths[a] - self.depths[b] >> i & 1:
                a = self.dbl[i][a]

        if a == b:
            return a

        for i in range(self.depths[a].bit_length())[::-1]:
            if self.dbl[i][a] == self.dbl[i][b]:
                continue
            a, b = self.dbl[i][a], self.dbl[i][b]
        return self.dbl[0][a]


lca = LowestCommonAncestor(g)
for a, b in edges:
    ans = 0
    ancestor = lca.lca(a, b)
    ans = lca.depths[a] + lca.depths[b] - 2 * lca.depths[ancestor] + 1
    print(ans)
