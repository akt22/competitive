from math import ceil
A, B, W = list(map(int, input().split()))
W = W * 1000

for i in range(A, B + 1):
    if W % i == 0:
        print(ceil(W / B), W // A)
        exit()
print("UNSATISFIABLE")
