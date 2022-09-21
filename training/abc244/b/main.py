N = int(input())
T = input()

dxdy = [
    (1, 0),
    (0, -1),
    (-1, 0),
    (0, 1),
]

x, y = 0, 0
direction = 0

for c in T:
    if c == "R":
        direction = (direction + 1) % 4
    else:
        dx, dy = dxdy[direction]
        x += dx
        y += dy
print(x, y)
