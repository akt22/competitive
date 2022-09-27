from collections import Counter

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = Counter(A)
for b in B:
    if b not in cnt or cnt[b] == 0:
        print("No")
        exit()
    cnt[b] -= 1
print("Yes")
