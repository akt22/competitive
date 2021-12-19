N = int(input())

c = 4
d = 7

for i in range(26):
    cost = c * i
    rest = N - cost
    if rest < 0:
        break
    if rest % d == 0:
        print("Yes")
        exit()
print("No")
