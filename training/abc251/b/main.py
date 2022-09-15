from itertools import combinations

N, W = list(map(int, input().split()))
A = list(map(int, input().split()))

one = [a for a in A if a <= W]

two = set()
for a, b in combinations(one, 2):
    if a + b <= W:
        two.add(a + b)

three = set()
for a, b, c in combinations(one, 3):
    if a + b + c <= W:
        three.add(a + b + c)

print(len(set(one) | two | three))
