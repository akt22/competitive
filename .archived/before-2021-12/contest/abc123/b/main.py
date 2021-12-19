foods = [input() for _ in range(5)]

min_idx = 0
min_digit = 9
for idx, food in enumerate(foods):
    digit = int(food[-1])
    if digit < min_digit and digit != 0:
        min_idx = idx
        min_digit = digit

ans = 0
for idx, food in enumerate(foods):
    digit = int(food[-1])
    if idx == min_idx or digit == 0:
        ans += int(food)
    else:
        ans += int(food) + 10 - digit
print(ans)
