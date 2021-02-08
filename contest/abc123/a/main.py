antennas = [int(input()) for _ in range(5)]
k = int(input())

cur = antennas[0]
for a in antennas[1:]:
    if a - cur > k:
        print(":(")
        exit()
print("Yay!")
