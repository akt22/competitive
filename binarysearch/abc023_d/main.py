N = int(input())

balloons = [list(map(int, input().split())) for _ in range(N)]


def check(line):
    l = []
    for h, s in balloons:
        l.append((line - h) // s)
    l.sort()
    for t, b in enumerate(l):
        if t > b:
            return False
    return True


ans = 10**14
over = 0
while abs(ans - over) > 1:
    mid = (ans + over) // 2
    if check(mid):
        ans = mid
    else:
        over = mid
print(ans)
