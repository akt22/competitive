from itertools import accumulate

D = int(input())
N = int(input())

attendances = [0] * (D + 1)
for _ in range(N):
    l, r = map(int, input().split())
    attendances[l - 1] += 1
    attendances[r] -= 1
acc = list(accumulate(attendances))
print(*acc[:-1], sep='\n')
