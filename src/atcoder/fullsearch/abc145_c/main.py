from collections import defaultdict
from itertools import combinations, permutations
from math import sqrt

N = int(input())

towns = [list(map(int, input().split())) for _ in range(N)]


distances = defaultdict(dict)
for a, b in combinations(range(N), 2):
    ax, ay = towns[a]
    bx, by = towns[b]
    distances[a][b] = sqrt((ax - bx)**2 + (ay - by)**2)
    distances[b][a] = sqrt((ax - bx)**2 + (ay - by)**2)

cnt = 0
total = 0
for path in permutations(range(N)):
    cnt += 1
    current = path[0]
    for n in path[1:]:
        total += distances[current][n]
        current = n

print(total / cnt)
