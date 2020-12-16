from decimal import Decimal

P = float(input())


def f(x): return Decimal(x) + (Decimal(P) / (2 ** (Decimal(x) / Decimal(1.5))))


low = 0.0
high = 10**5
for _ in range(500):
    c1 = ((low * 2) + high) / 3
    c2 = (low + (high * 2)) / 3
    if f(c1) > f(c2):
        low = c1
    else:
        high = c2
print(f(low))
