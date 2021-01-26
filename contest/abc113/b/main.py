N = int(input())
T, A = map(int, input().split())
H = map(int, input().split())

ans_idx = -1
min_diff = 10**10
for idx, h in enumerate(H):
    temp = T - h * 0.006
    diff = abs(temp - A)
    # print(f"{temp=}, {diff=}")
    if min_diff > diff:
        ans_idx = idx + 1
        min_diff = diff
print(ans_idx)
