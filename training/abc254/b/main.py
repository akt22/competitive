N = int(input())

prev = [1]
print(1)

for i in range(1, N):
    curr = [1]
    for j in range(1, (i + 1) // 2):
        curr.append(prev[j - 1] + prev[j])
    if i % 2 == 1:
        curr.extend(curr[::-1])
    else:
        curr.extend([prev[(i // 2) - 1] + prev[i // 2], *curr[::-1]])
    print(*curr)
    prev = curr
