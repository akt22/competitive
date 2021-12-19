s = int(input())

seen = set()


def f(n):
    return n // 2 if n % 2 == 0 else (3 * n) + 1


n = s
idx = 0
seen.add(n)
while True:
    idx += 1
    new = f(n)
    if new in seen:
        print(idx + 1)
        exit()
    n = new
    seen.add(n)
