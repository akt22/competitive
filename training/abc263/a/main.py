from collections import Counter

cnt = Counter(list(map(int, input().split())))

if len(cnt) == 2 and cnt.most_common()[0][1] == 3:
    print('Yes')
else:
    print('No')
