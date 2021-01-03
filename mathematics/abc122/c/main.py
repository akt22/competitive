N, Q = map(int, input().split())
S = input()
queries = [list(map(int, input().split())) for _ in range(Q)]

s = [0] * (N + 1)

for i in range(N - 1):
    if S[i] == "A" and S[i + 1] == "C":
        s[i + 1] = s[i] + 1
    else:
        s[i + 1] = s[i]

s.insert(0, 0)

for l, r in queries:
    print(s[r] - s[l])
