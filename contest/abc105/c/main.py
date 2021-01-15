N = int(input())

if N == 0:
    print("0")
    exit()

ans = []
while N != 0:
    r = 0 if N % (-2) == 0 else 1
    N = (N - r) // (-2)
    ans.append(str(r))
print("".join(reversed(ans)))
