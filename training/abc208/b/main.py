from math import factorial

P = int(input())
coins = list(map(factorial, range(1, 11)))

ans = 0
for coin in coins[::-1]:
    payed = P // coin
    P -= coin * min(100, payed)
    ans += min(100, payed)
print(ans)
