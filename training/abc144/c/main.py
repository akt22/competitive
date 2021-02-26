N = int(input())

i = 1
ans = 1 << 60
while i * i <= N:
    if N % i == 0:
        ans = min(ans, (i - 1) + ((N // i) - 1))
    i += 1
print(ans)
