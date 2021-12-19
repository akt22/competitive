sx, sy, tx, ty = list(map(int, input().split()))
x = tx - sx
y = ty - sy

first = "U" * y + "R" * x
second = "D" * y + "L" * x
third = "L" + "U" * (y + 1) + "R" * (x + 1) + "D"
forth = "R" + "D" * (y + 1) + "L" * (x + 1) + "U"

print(first + second + third + forth)
