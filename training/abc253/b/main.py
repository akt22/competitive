H, W = list(map(int, input().split()))

p = []
for i in range(H):
    for j, c in enumerate(input()):
        if c == "o":
            p.append((i, j))

print(abs(p[0][0] - p[1][0]) + abs(p[0][1] - p[1][1]))
