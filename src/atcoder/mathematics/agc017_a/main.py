from math import sqrt

N = int(input())

for i in range(2, int(sqrt(N)) + 1):
    if i != 2 and i % 2 == 0:
        continue

    if N % i == 0:
        print("NO")
        exit()

print("YES")
