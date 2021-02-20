X = input()
M = int(input())

n = int(max(list(X)))


def trans(x, n):
    out = 0
    for i in range(1, len(str(x)) + 1):
        out += int(x[-i]) * (n**(i - 1))
    return out


if len(X) == 1:
    if int(trans(X, n)) > M:
        print(0)
    else:
        print(1)
else:
    start = n
    end = 10**18 + 1
    while end - start > 1:
        mid = (start + end) // 2
        if int(trans(X, mid)) > M:
            end = mid
        elif int(trans(X, mid)) <= M:
            start = mid
    print(start - n)
