S = int(input())

base = 10**9

q = S // base + 1
r = base * q - S


if S == 10**18:
    print(f"0 0 {base} 0 0 {base}")
else:
    print(f"0 0 {base} 1 {r} {q}")
