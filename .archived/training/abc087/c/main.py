from itertools import accumulate

N = int(input())
S1 = list(accumulate(list(map(int, input().split())), initial=0))
S2 = list(accumulate(list(map(int, input().split())), initial=0))

ans = 0

for i in range(1, N + 1):
    c = S1[i] + (S2[-1] - S2[i - 1])
    ans = max(ans, c)

print(ans)
