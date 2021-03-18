N, A, B = list(map(int, input().split()))

if A > B:
    print(0)
    exit()
if N == 1 and A != B:
    print(0)
    exit()

ma = B * (N - 1) + A
mi = A * (N - 1) + B
print(ma - mi + 1)
