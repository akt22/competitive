X, Y, Z = list(map(int, input().split()))

if (X < Y < 0 or 0 < Y < X):
    if not (0 > Y > Z or Z > Y > 0):
        ans = abs(Z)
        ans += abs(Z - X)
    else:
        print(-1)
        exit()
else:
    ans = abs(X)

print(ans)
