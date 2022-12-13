N = int(input())
A = list(map(int, input().split()))

even, odd = [], []

for a in A:
    if a % 2 == 0:
        even.append(a)
    else:
        odd.append(a)

even.sort()
odd.sort()

if len(even) > 1 and len(odd) > 1:
    print(max(even[-1] + even[-2], odd[-1] + odd[-2]))
elif len(even) > 1:
    print(even[-1] + even[-2])
elif len(odd) > 1:
    print(odd[-1] + odd[-2])
else:
    print(-1)
