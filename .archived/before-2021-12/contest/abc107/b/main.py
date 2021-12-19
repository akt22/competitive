H, W = map(int, input().split())

mazes = []
for _ in range(H):
    mazes.append(input())

r = "." * W
mazes2 = []
for row in mazes:
    if r == row:
        continue
    mazes2.append(row)

c = "." * len(mazes2)
mazes3 = []
for x in range(len(mazes2[0])):
    tmp = ""
    for y in range(len(mazes2)):
        tmp += mazes2[y][x]
    if tmp == c:
        continue
    mazes3.append(tmp)

for y in range(len(mazes3[0])):
    for x in range(len(mazes3)):
        print(mazes3[x][y], end="")
    print()
