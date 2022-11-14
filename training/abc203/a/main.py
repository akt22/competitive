from collections import Counter

cnt = Counter(list(map(int, input().split())))

if len(cnt) == 3:
    print(0)
elif len(cnt) == 2:
    print(cnt.most_common(2)[-1][0])
else:
    print(cnt.most_common(1)[0][0])
