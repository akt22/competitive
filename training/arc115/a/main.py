from collections import Counter
N, M = list(map(int, input().split()))
S = [Counter(list(input())) for _ in range(N)]

even, odd = 0, 0
for s in S:
    if s["1"] % 2 == 0:
        even += 1
    else:
        odd += 1
print(even * odd)
