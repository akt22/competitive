def main():
    ans = 0
    p = -float('inf')
    for x, l in sorted(robots, key=lambda x: x[0] + x[1]):
        if x - l >= p:
            p = x + l
            ans += 1
    print(ans)


if __name__ == "__main__":
    N = int(input().strip())
    robots = []
    for _ in range(N):
        robots.append(list(map(int, input().strip().split(" "))))
    main()
