import bisect

A, B, Q = map(int, input().split())
S = [-10**12] + [int(input()) for _ in range(A)]  + [10**12]
T = [-10**12] + [int(input()) for _ in range(B)] + [10**12]
X = [int(input()) for _ in range(Q)]

S.sort()
T.sort()

for x in X:
    s_idx = bisect.bisect_right(S, x)
    t_idx = bisect.bisect_right(T, x)
    ans = 10 ** 12

    # s -> t
    ans = min(ans, abs(S[s_idx] - x) + abs(T[t_idx] - S[s_idx]))
    ans = min(ans, abs(S[s_idx] - x) + abs(T[t_idx - 1] - S[s_idx]))
    ans = min(ans, abs(S[s_idx - 1] - x) + abs(T[t_idx] - S[s_idx - 1]))
    ans = min(ans, abs(S[s_idx - 1] - x) + abs(T[t_idx - 1] - S[s_idx - 1]))
    # t -> s
    ans = min(ans, abs(T[t_idx] - x) + abs(S[s_idx] - T[t_idx]))
    ans = min(ans, abs(T[t_idx] - x) + abs(S[s_idx - 1] - T[t_idx]))
    ans = min(ans, abs(T[t_idx - 1] - x) + abs(S[s_idx] - T[t_idx - 1]))
    ans = min(ans, abs(T[t_idx - 1] - x) + abs(S[s_idx - 1] - T[t_idx - 1]))
    print(ans)
