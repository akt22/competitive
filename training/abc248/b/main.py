A, B, K = list(map(int, input().split()))

ans = 0
while A < B:
    A *= K
    ans += 1
print(ans)
