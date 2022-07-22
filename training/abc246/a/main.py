from collections import defaultdict

x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
x3, y3 = list(map(int, input().split()))


dx = defaultdict(int)
dy = defaultdict(int)
dx[x1] += 1
dy[y1] += 1
dx[x2] += 1
dy[y2] += 1
dx[x3] += 1
dy[y3] += 1

x, y = 0, 0
for k, v in dx.items():
    if v == 1:
        x = k

for k, v in dy.items():
    if v == 1:
        y = k
print(x, y)
