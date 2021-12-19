from collections import Counter

N, A, B = list(map(int, input().split()))
S = input()
cnt = Counter(S)

p = 0
b = 0
for s in S:
    if p >= A + B:
        print("No")
        continue
    if s == "c":
        print("No")
        continue
    elif s == "a":
        print("Yes")
        p += 1
    elif s == "b" and b < B:
        print("Yes")
        p += 1
        b += 1
    else:
        print("No")
