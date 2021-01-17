S = int(input())
K = int(input())

first_num = "1"
idx = 0
for _idx, s in enumerate(str(S)):
    if s == "1":
        continue
    else:
        first_num = s
        idx = _idx
        break

if idx >= K:
    print("1")
else:
    print(first_num)
