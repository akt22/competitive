N = int(input())
stocks = list(map(int, input().split()))

cur = 1000
for i in range(N - 1):
    stock = 0
    if stocks[i] < stocks[i + 1]:
        stock += cur // stocks[i]
    cur += (stocks[i + 1] - stocks[i]) * stock
print(cur)
