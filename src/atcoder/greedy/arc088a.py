def main():
    ans = 0
    cur = X
    while cur <= Y:
        cur *= 2
        ans += 1
    print(ans)
    exit(0)


if __name__ == "__main__":
    X, Y = map(int, input().strip().split(" "))
    main()
