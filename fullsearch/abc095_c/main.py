A, B, C, X, Y = map(int, input().split())


price = 0
mi = min(X, Y)
price += 2 * mi * C
if X > Y:
    price += A * (X - Y)
elif X < Y:
    price += B * (Y - X)

price1 = 0
ma = max(X, Y)
price1 += 2 * ma * C

price2 = 0
price2 += A * X
price2 += B * Y

print(min(price, price1, price2))
