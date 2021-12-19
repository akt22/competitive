N = int(input())
A = list(map(int, input().split()))

minus_cnt = 0
minimum = 10**10
ans = 0
for a in A:
    if a < 0:
        minus_cnt += 1
    ans += abs(a)
    minimum = min(minimum, abs(a))

if minus_cnt % 2 == 0:
    print(ans)
else:
    print(ans - 2 * minimum)
