from collections import Counter

S = input()
cnt = Counter(S)

print(S.find(cnt.most_common()[-1][0]) + 1)
