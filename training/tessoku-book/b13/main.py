from itertools import accumulate

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

acc = list(accumulate(A, initial=0))

end = 0
ans = 0

for start, elem in enumerate(acc):
    while end < N and acc[end + 1] - elem <= K:
        end += 1
    ans += end - start
print(ans)
