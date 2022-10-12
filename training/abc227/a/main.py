N, K, A = list(map(int, input().split()))

A -= 1
K -= 1
print(((A + K) % N) + 1)
