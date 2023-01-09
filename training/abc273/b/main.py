from decimal import Decimal, ROUND_HALF_UP

X, K = input().split()
X = Decimal(X)
K = int(K)

if 10**(K - 1) > X:
    print(0)
    exit()

for i in range(K):
    X = X.quantize(Decimal(f"1E{i+1}"), rounding=ROUND_HALF_UP)
print(f"{X:.0f}")
