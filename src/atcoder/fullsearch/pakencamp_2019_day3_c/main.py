from itertools import combinations

N, M = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(N)]


max_score = 0
for a, b in combinations(range(0, M), 2):
    score = 0
    for point in points:
        score += max(point[a], point[b])
    max_score = max(max_score, score)
print(max_score)
