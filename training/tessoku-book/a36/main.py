N, K = list(map(int, input().split()))

if K < 2 * N:
    print("No")
    exit()

if K % 2 == 0:
    print("Yes")
else:
    print("No")
