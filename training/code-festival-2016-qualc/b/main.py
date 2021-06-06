from heapq import heappush, heappop

K, T = list(map(int, input().split()))
A = list(map(int, input().split()))

h = []
for idx, a in enumerate(A):
    heappush(h, (-a, idx))

ans = 0
prev = None
while h:
    a, idx = heappop(h)
    if prev == idx and len(h) > 0:
        na, nidx = heappop(h)
        if na + 1 < 0:
            heappush(h, (na + 1, nidx))
        heappush(h, (a, idx))
        prev = nidx
    elif prev == idx:
        ans += -a
        break
    else:
        if a + 1 < 0:
            heappush(h, (a + 1, idx))
        prev = idx
print(ans)
