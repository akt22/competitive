N = int(input())
S = input()

for idx, c in enumerate(S):
    if c == "1":
        print("Takahashi" if idx % 2 == 0 else "Aoki")
        exit()
