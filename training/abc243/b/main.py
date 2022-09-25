N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans1 = set()
for i in range(N):
    if A[i] == B[i]:
        ans1.add(A[i])
print(len(ans1))

print(len((set(A) & set(B)) - ans1))
