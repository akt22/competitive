N = int(input())
query = [input().split() for _ in range(N)]

quotient = 10000

ans = 0
for t, a in query:
    A = int(a)
    if t == "+":
        ans += A
    elif t == "-":
        ans -= A
    else:
        ans *= A % quotient
    ans %= quotient
    print(ans)
