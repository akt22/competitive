N = int(input())
A = set(map(int, input().split()))

if set(range(1, N + 1)) == A:
    print("Yes")
else:
    print("No")
