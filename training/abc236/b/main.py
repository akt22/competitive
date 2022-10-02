from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cnt = Counter(A)

for k, v in cnt.items():
    if v == 3:
        print(k)
        exit()
