from itertools import combinations
from collections import Counter

N = int(input())
hats = list(map(int, input().split()))
cnt = Counter(hats)

if len(cnt) == 1 and 0 in cnt:
    print("Yes")
    exit()
if len(cnt) > 3 or len(cnt) == 1:
    print("No")
    exit()

# 要素数が3なら、必ず同じ数出現してることが条件
if len(cnt) == 3 and len(set(cnt.values())) != 1:
    print("No")
    exit()
# 要素数が2なら、出現数がいい感じじゃないとだめ
if len(cnt) == 2:
    a, b = sorted(cnt.values())
    if 0 not in cnt or b % a != 0:
        print("No")
        exit()

for h1, h2 in combinations(cnt.keys(), 2):
    if h1 ^ h2 not in cnt:
        print("No")
        exit()
print("Yes")
