S = input()

corpus = ["A", "C", "G", "T"]
max_cnt = 0
cnt = 0
for s in S:
    if s in corpus:
        cnt += 1
    else:
        cnt = 0
    max_cnt = max(max_cnt, cnt)
print(max_cnt)
