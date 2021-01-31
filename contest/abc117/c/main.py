N, M = map(int, input().split())
X = list(map(int, input().split()))

if N >= M:
    print('0')
    exit()

X.sort()
l = []
for i in range(M - 1):
    l.append(X[i + 1] - X[i])
l.sort(reverse=True)
print(sum(l[(N - 1):]))
