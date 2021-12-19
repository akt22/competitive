N, K = list(map(int, input().split()))

cand = []
for e in range(2, 2 * N + 1):
    f = e + K
    if 2 <= f <= 2 * N:
        cand.append([f, e])

ans = 0
for e, f in cand:
    left = max(e - N, 1)
    right = max(min(e - 1, N), 1)
    e_comb = right - left + 1
    left = max(f - N, 1)
    right = max(min(f - 1, N), 1)
    f_comb = right - left + 1
    ans += e_comb * f_comb
print(ans)
