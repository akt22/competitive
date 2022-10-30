N = int(input())

k = 0
while True:
    if 2**k > N:
        print(k - 1)
        exit()
    k += 1
