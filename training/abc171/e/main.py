N = int(input())
A = list(map(int, input().split()))

base = 0
for a in A:
    base ^= a

ans = []
for a in A:
    ans.append(base ^ a)
print(*ans)
