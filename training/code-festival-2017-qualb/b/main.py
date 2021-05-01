from collections import Counter

N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

d_cnt = Counter(D)
t_cnt = Counter(T)

if t_cnt - d_cnt:
    print("NO")
else:
    print("YES")
