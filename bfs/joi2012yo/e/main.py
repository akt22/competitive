from collections import deque

W, H = map(int, input().split())

m = [[0] * (W + 2) for _ in range(H + 2)]
visited = [[False] * (W + 2) for _ in range(H + 2)]

for x in range(H):
    for y, v in enumerate(map(int, input().split())):
        m[x + 1][y + 1] = v

moves = [
    [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1)],  # even
    [(-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (1, 1)]  # odd
]

q = deque()
q.append([0, 0])

cnt = 0

while q:
    x, y = q.popleft()

    for dx, dy in moves[y % 2]:
        nx, ny = x + dx, y + dy
        if ny < 0 or ny > H + 1 or nx < 0 or nx > W + 1:
            continue
        if m[ny][nx] == 1:
            cnt += 1
        else:
            if not visited[ny][nx]:
                visited[ny][nx] = True
                q.append([nx, ny])

print(cnt)
