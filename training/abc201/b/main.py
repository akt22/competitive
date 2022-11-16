N = int(input())
mountains = []
for _ in range(N):
    s, t = input().split()
    mountains.append([s, int(t)])

print(sorted(mountains, key=lambda x: x[1])[-2][0])
