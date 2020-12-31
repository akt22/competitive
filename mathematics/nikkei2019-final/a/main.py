from itertools import accumulate

N = int(input())
blocks = list(map(int, input().split()))


acc = list(accumulate(blocks))
acc.insert(0, 0)

for i in range(1, N + 1):
    tmp = []
    for j in range(N - i + 1):
        tmp.append(acc[i + j] - acc[j])
    print(max(tmp))
