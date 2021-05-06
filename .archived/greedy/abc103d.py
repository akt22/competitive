def main():
    dropped = float('inf')
    ans = 0
    for a, b in sorted(wishes, key=lambda x: x[1]):
        if dropped != float('inf') and a <= dropped:
            continue
        else:
            dropped = b - 1
            ans += 1
    print(ans)


if __name__ == "__main__":
    N, M = map(int, input().strip().split(" "))
    wishes = []
    for _ in range(M):
        wishes.append(list(map(int, input().strip().split(" "))))
    main()
