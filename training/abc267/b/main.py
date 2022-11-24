S = input()

if S[0] == "1":
    print("No")
    exit()

rows = [
    S[6],
    S[3],
    S[1] + S[7],
    S[0] + S[4],
    S[2] + S[8],
    S[5],
    S[9],
]

for i in range(5):
    flg = False
    for j in range(i + 1, 7):
        if "1" not in rows[j]:
            flg = True
            continue
        if "1" in rows[i] and "1" in rows[j] and flg:
            print("Yes")
            exit()
print("No")
