from decimal import Decimal, ROUND_HALF_UP

X = Decimal(float(input()))
print(X.quantize(Decimal(1), ROUND_HALF_UP))
