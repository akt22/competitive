from math import ceil, floor
A, B, W = list(map(int, input().split()))
W = W * 1000

if ceil(W / B) > floor(W / A):
    print("UNSATISFIABLE")
else:
    print(ceil(W / B), floor(W / A))
