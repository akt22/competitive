N = int(input())

L = list(map(int, input().split()))

longest = max(L)
s = sum(L)
if (s - longest) > longest:
    print("Yes")
else:
    print("No")
