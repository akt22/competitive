N = int(input())
P = list(map(int, input().split()))

s = set()

ans = 0
for p in P:
    s.add(p)
    while ans in s:
        ans += 1
    print(ans)
