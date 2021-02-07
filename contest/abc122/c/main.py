N, Q = map(int, input().split())
S = input()

queries = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(Q)]

acc = [0]
cnt = 0
for idx, s in enumerate(S[:-1]):
    if s == "A" and S[idx + 1] == "C":
        cnt += 1
    acc.append(cnt)

for l, r in queries:
    print(acc[r] - acc[l])
