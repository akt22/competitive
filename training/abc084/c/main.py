N = int(input())
trains = [list(map(int, input().split())) for _ in range(N - 1)]

for i, (c, s, f) in enumerate(trains):
    ans = s + c
    for j, (cj, sj, fj) in enumerate(trains[i + 1:]):
        if ans >= sj:
            if ans % fj != 0:
                ans += fj - ans % fj
        else:
            ans = sj
        ans += cj
    print(ans)
print(0)
