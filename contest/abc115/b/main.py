N = int(input())
P = [int(input()) for _ in range(N)]

m = max(P)
s = sum(P)
print(s - m // 2)
