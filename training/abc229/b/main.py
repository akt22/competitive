A, B = list(input().split())

digit = min(len(A), len(B))

for i in range(1, digit + 1):
    a, b = A[-i], B[-i]
    if int(a) + int(b) > 9:
        print("Hard")
        exit()
print("Easy")
