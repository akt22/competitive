N, A, B = list(map(int, input().split()))


a = ""
b = ""
for i in range(N * B):
    if (i // B) % 2 == 0:
        a += "."
        b += "#"
    else:
        a += "#"
        b += "."

for i in range(N * A):
    if (i // A) % 2 == 0:
        print(a)
    else:
        print(b)
