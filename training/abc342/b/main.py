N = int(input())
P = list(map(int, input().split()))
Q = int(input())

q = []
for _ in range(Q):
    q.append(list(map(int, input().split())))

for a, b in q:
    ia, ib = 0, 0
    for idx, p in enumerate(P):
        if a == p:
            ia = idx
        if b == p:
            ib = idx
    print(a if ia < ib else b)
