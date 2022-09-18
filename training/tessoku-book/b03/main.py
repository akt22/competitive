N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        for k in range(N):
            if i == k or j == k:
                continue
            if A[i] + A[j] + A[k] == 1000:
                print("Yes")
                exit()
print("No")
