import sys

sys.setrecursionlimit(10**6)

island = []


def rpl(s, c, idx):
    return s[:idx] + c + s[idx+1:]


def dfs(x, y, _island):
    if not 0 <= y < 10 or not 0 <= x < 10 or _island[y][x] != "o":
        return

    _island[y] = rpl(_island[y], "#", x)

    dfs(x-1, y, _island)
    dfs(x+1, y, _island)
    dfs(x, y-1, _island)
    dfs(x, y+1, _island)


def solve(cnt):
    for y, row in enumerate(island):
        for x, _ in enumerate(row):
            _cnt = 0
            _island = island.copy()
            _island[y] = rpl(_island[y], "o", x)

            dfs(x, y, _island)

            for _row in _island:
                _cnt += _row.count("#")

            if cnt + 1 == _cnt:
                print("YES")
                exit(0)

    print("NO")


def main():
    cnt = 0
    for i in range(10):
        island.append(input().strip())

    for row in island:
        cnt += row.count("o")

    solve(cnt)

if __name__ == "__main__":
    main()
