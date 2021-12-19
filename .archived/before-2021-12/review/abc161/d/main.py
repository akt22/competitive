from collections import deque

K = int(input())
q = deque(list(range(1, 10)))

for _ in range(K):
    v = q.popleft()
    mod = v % 10
    if mod != 0:
        q.append(10 * v + mod - 1)
    q.append(10 * v + mod)
    if mod != 9:
        q.append(10 * v + mod + 1)
print(v)
