def main():
    ans = 0
    change = 1000 - payed

    for coin in coins:
        t = change // coin
        change -= t * coin
        ans += t
    print(ans)

if __name__ == "__main__":
    payed = int(input().strip())

    coins = [500, 100, 50, 10, 5, 1]

    main()
