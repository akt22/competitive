N = int(input())

ans = ""
while N > 0:
    mod = N % 2
    ans += str(mod)
    N //= 2

print(ans[::-1].zfill(10))
