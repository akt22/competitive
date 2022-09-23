N = int(input())
A = list(map(int, input().split()))

ans = 0
right = 0

for left, a in enumerate(A):
    ans += 1
    while right < N - 1 and A[right] < A[right + 1] and left <= right:
        right += 1
    ans += right - left
    if right == left:
        right += 1
print(ans)
