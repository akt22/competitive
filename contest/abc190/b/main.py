N, S, D = map(int, input().split())
spels = [list(map(int, input().split())) for _ in range(N)]

for x, y in spels:
    if x >= S or y <= D:
        continue
    else:
        print("Yes")
        exit()
print("No")
