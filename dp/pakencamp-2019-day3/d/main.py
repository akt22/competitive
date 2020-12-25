N = int(input())


def pp(_flag):
    for y in range(5):
        for x in range(N):
            print(_flag[y][x], end=" ")
        print()


flag = [list(input()) for _ in range(5)]
pp(flag)
