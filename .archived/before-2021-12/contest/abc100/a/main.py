A, B = map(int, input().split())

cake = [-1] * 16

a, b = 0, 0
for i in range(16):
    left = i - 1
    right = i + 1 if i != 15 else 0
    if cake[i] == -1 and a < A and (cake[left] != 1 and cake[right] != 1):
        a += 1
        cake[i] = 1
    if cake[i] == -1 and b < B and (cake[left] != 2 and cake[right] != 2):
        b += 1
        cake[i] = 2
    if a >= A and b >= B:
        print("Yay!")
        exit()

print(":(")
