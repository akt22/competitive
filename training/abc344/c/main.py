N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
L = int(input())
C = list(map(int, input().split()))
Q = int(input())
X = list(map(int, input().split()))

pool = set()

for a in A:
    for b in B:
        for c in C:
            pool.add(a + b + c)

for x in X:
    print("Yes" if x in pool else "No")
