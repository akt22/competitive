A1, A2, A3 = sorted(list(map(int, input().split())))
print("Yes" if A3 - A2 == A2 - A1 else "No")
