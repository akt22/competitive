N = int(input())

a = 2
ans = 0
memo = set()
while a * a <= N:
    for b in range(2, 10**10):
        if a**b <= N and a**b not in memo:
            ans += 1
            memo.add(a**b)
        else:
            break
    a += 1
print(N - ans)
