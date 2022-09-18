from collections import Counter

N = int(input())
names = []
st = []
for _ in range(N):
    s, t = input().split()
    names.append(s)
    if s != t:
        names.append(t)
    st.append((s, t))

cnt = Counter(names)

unique = sum([1 for s, t in st if cnt[s] == 1 or cnt[t] == 1])

if unique >= N:
    print('Yes')
else:
    print('No')
