V, T, S, D = map(int, input().split())

dist = V * T
vanish = V * (S - T) + dist

if dist <= D <= vanish:
    print("No")
else:
    print("Yes")
