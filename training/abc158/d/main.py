from collections import deque

S = input()
Q = int(input())
ops = []
for _ in range(Q):
    q = input()
    if q[0] == "1":
        ops.append(int(q))
    else:
        ops.append(q.split()[1:])

queue = deque(list(S))
rvs = 0
for op in ops:
    if type(op) == int:
        rvs += 1
    else:
        f, c = op
        if ((f == "1" and rvs % 2 == 0) or (f == "2" and rvs % 2 == 1)):
            queue.appendleft(c)
        else:
            queue.append(c)
if rvs % 2 == 1:
    queue.reverse()
print(*queue, sep="")
