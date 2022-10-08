from collections import Counter

N = int(input())
S = [input() for _ in range(N)]

votes = Counter(S)
print(votes.most_common(1)[0][0])
