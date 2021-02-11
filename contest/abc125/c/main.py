from math import gcd

N = int(input())
A = list(map(int, input().split()))

left = [0]
right = [0]
for i in range(N):
    left.append(gcd(left[-1], A[i]))
    right.append(gcd(right[-1], A[N - i - 1]))
right.reverse()
print(max(gcd(left[i], right[i + 1]) for i in range(N)))
