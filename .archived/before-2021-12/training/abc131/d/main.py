N = int(input())
tasks = [list(map(int, input().split())) for _ in range(N)]

tasks.sort(key=lambda x: x[1])

cur = 0
for a, b in tasks:
    cur += a
    if cur > b:
        print("No")
        exit()
print("Yes")
