import string

N, X = list(map(int, input().split()))

a = string.ascii_uppercase

print(a[(X - 1) // N])
