M = int(input())
sign = [list(map(int, input().split())) for _ in range(M)]

N = int(input())
cord = [list(map(int, input().split())) for _ in range(N)]

relative = []
base_x, base_y = sign[0]
for x, y in sign[1:]:
    relative.append([base_x - x, base_y - y])

for x, y in cord:
    flg = True
    for rx, ry in relative:
        nx, ny = x - rx, y - ry
        if [nx, ny] not in cord:
            flg = False
    if flg:
        print(f"{x - base_x} {y - base_y}")
        exit()
