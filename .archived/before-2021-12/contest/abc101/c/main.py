from math import ceil

N, K = map(int, input().split())
a = map(int, input().split())

print(ceil((N - 1) / (K - 1)))
