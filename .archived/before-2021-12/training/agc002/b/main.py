N, M = list(map(int, input().split()))
ops = [list(map(int, input().split())) for _ in range(M)]

boxes = [1] * N

ans = set([1])
for x, y in ops:
    boxes[x - 1] -= 1
    boxes[y - 1] += 1
    if x in ans:
        ans.add(y)
        if boxes[x - 1] == 0:
            ans.remove(x)
print(len(ans))
