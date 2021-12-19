A, B, X = list(map(int, input().split()))

if A >= X:
    print(0)
    exit()


def f(n):
    return A * n + B * len(str(n))


start, end = 0, X // A
mid = (end - start) // 2
for i in range(10):
    if end - mid < 10:
        break
    v = f(mid)
    if v > X:
        # mid以下
        start, end = start, mid
        mid = (end + start) // 2
    elif v < X:
        # mid以上
        start, end = mid, end
        mid = (end + start) // 2
    else:
        print(mid)
        exit()

ans = 0
for i in range(start, end):
    v = f(i)
    if v > X:
        break
    else:
        if 10**9 <= i <= v <= X:
            print(10**9)
            exit()
        ans = i
print(ans)
