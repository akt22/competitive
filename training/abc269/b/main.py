S = [list(input()) for _ in range(10)]

A, B, C, D = None, None, None, None
for i, row in enumerate(S):
    if "#" in row and A is None:
        A = i + 1
    elif "#" not in row and A is not None and B is None:
        B = i
    for j, c in enumerate(row):
        if c == "#" and C is None:
            C = j + 1
        elif c == "." and C is not None and D is None:
            D = j
print(A, B if B else 10)
print(C, D if D else 10)
