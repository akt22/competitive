N = int(input())


def enum_divisors(n):
    res = []
    i = 0
    while i * i <= n:
        i += 1
        if n % i == 0:
            res.append(i)
            if n // i != i:
                res.append(n // i)
    return sorted(set(res))


div = enum_divisors(N)
size = len(div)
mid = size // 2

if size < 2:
    print(1)
elif size % 2 == 0:
    a = div[mid]
    b = div[mid - 1]
    print(max(len(str(a)), len(str(b))))
else:
    # (約数が奇数 = 平方数) なので a**2 = N
    print(len(str(div[mid])))
