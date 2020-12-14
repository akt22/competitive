import bisect

N = int(input())

A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))
C = sorted(map(int, input().split()))

cnt = 0
for b in B:
    a = bisect.bisect_left(A, b)
    c = bisect.bisect_right(C, b)
    cnt += a * (N - c)
print(cnt)
