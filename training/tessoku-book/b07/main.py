from itertools import accumulate

T = int(input())
N = int(input())

attendances = [0] * (T + 1)
for _ in range(N):
    l, r = list(map(int, input().split()))
    attendances[l] += 1
    attendances[r] -= 1

acc = list(accumulate(attendances))

print(*acc[:-1], sep="\n")
