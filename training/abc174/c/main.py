K = int(input())

a = [7]

if K == 7 or K == 1:
    print(1)
    exit()

for i in range(1, K + 1):
    a.append((10 * a[i - 1] + 7) % K)

for idx, aa in enumerate(a):
    if aa == 0:
        print(idx + 1)
        exit()
print(-1)
