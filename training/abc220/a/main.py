A, B, C = list(map(int, input().split()))

mi = A // C if A % C == 0 else A // C + 1
print(mi * C if mi * C <= B else -1)
