H, W, N = list(map(int, input().split()))
T = input()
S = [input() for _ in range(H)]


def simulation(i, j):
    for t in T:
        if t == "L":
            j -= 1
        elif t == "R":
            j += 1
        elif t == "U":
            i -= 1
        else:
            i += 1
        if S[i][j] == "#":
            return 0
    return 1


ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            ans += simulation(i, j)

print(ans)
