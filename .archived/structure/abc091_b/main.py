from collections import defaultdict

N = int(input())
blues = [input() for _ in range(N)]
M = int(input())
reds = [input() for _ in range(M)]

ans = defaultdict(int)

for blue in blues:
    ans[blue] += 1

for red in reds:
    ans[red] -= 1

a = max(ans.values())
if a >= 0:
    print(a)
else:
    print("0")
