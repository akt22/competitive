a, b, c = list(map(int, input().split()))

m = sorted([a, b, c])[1]
print("Yes" if m == b else "No")
