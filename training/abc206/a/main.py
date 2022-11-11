from math import floor

N = int(input())
price = floor(N * 1.08)

if price > 206:
    print(":(")
elif price == 206:
    print("so-so")
else:
    print("Yay!")
