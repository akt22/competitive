from collections import defaultdict


def dfs(u, parent):
    if visited[u]:
        return False
    visited[u] = True

    flg = True
    for dest in inputs[u]:
        if dest == parent:
            continue
        flg = dfs(dest, u) and flg
    return flg


def solve():
    ans = 0
    for u in inputs:
        if not visited[u]:
            if dfs(u, -1):
                ans += 1

    print(ans)


if __name__ == "__main__":
    N, M = list(map(int, input().strip().split(" ")))
    inputs = {}
    for i in range(N):
        inputs[i] = []
    visited = [False] * N
    for i in range(M):
        u, v = list(map(int, input().strip().split(" ")))
        inputs[u-1].append(v-1)
        inputs[v-1].append(u-1)
    solve()
