N, L = list(map(int, input().split()))
K = int(input())
A = list(map(int, input().split()))


def solve(m):
    cnt, prev = 0, 0
    for a in A:
        if a - prev >= m and L - a >= m:
            cnt += 1
            prev = a
    return True if cnt >= K else False


left = -1
right = L + 1
while right - left > 1:
    mid = left + (right - left) // 2
    if solve(mid) == False:
        right = mid
    else:
        left = mid
print(left)
