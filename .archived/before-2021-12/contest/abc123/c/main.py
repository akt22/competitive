N = int(input())
trans = [int(input()) for _ in range(5)]

bottleneck = min(trans)
if bottleneck != 1:
    print(N // bottleneck + 5)
else:
    print(N // bottleneck + 4)
