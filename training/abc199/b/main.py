N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ma = max(A)
mb = min(B)
print(max(mb - ma + 1, 0))
