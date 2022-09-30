N = int(input())
A = list(map(int, input().split()))

acc = [0]
for a in A:
    acc.append((acc[-1] + a) % 360)
acc.append(360)
acc.sort()

ans = 0
for i in range(N + 1, 0, -1):
    ans = max(ans, acc[i] - acc[i - 1])
print(ans)
