N, X = list(map(int, input().split()))
A = list(map(int, input().split()))

print("Yes" if X >= (sum(A) - N // 2) else "No")
