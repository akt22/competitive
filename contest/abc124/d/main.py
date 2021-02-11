from itertools import accumulate, groupby

N, K = map(int, input().split())
S = input()

nums = []
if S[0] == "0":
    nums.append(0)

# 0 と 1 の数を交互にnumsにappend
# numsは偶数個目は連続する1の個数、奇数個目は連続する0の個数になる
# 0 1 00 1 000 11 00 1 0 1
# nums: 0 1 2 1 3 2 2 1 1 1
for _, g in groupby(S):
    nums.append(len(list(g)))

if S[-1] == "0":
    nums.append(0)

sums = list(accumulate(nums, initial=0))

# 偶数個目の要素のうち、長さ2K+1以下の区間の総和の最大値を求める
# 2K -> 0と1が混じってるので
ans = 0
for left in range(0, len(sums), 2):
    right = left + K * 2 + 1
    if right >= len(sums):
        right = len(sums) - 1
    ans = max(ans, sums[right] - sums[left])
print(ans)
