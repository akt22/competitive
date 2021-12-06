N, M = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(N)]

prev = None
for i, row in enumerate(matrix):
    f = 0
    _i = 0
    for j, num in enumerate(row):
        if j == 0:
            if i != 0 and num != matrix[i - 1][j] + 7:
                print("No")
                exit()
            f = num
            _i = num // 7 if num % 7 != 0 else num // 7 - 1
            continue
        if num != f + j:
            print("No")
            exit()
        if _i != num // 7 and num % 7 != 0:
            print("No")
            exit()
print("Yes")
