N = int(input())


def solve(n):
    if n <= 26:
        return chr(64 + n)
    elif n % 26 == 0:
        return solve(n // 26 - 1) + chr(90)
    else:
        return solve(n // 26) + chr(64 + n % 26)


print(solve(N).lower())
