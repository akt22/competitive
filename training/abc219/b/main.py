S = [input() for _ in range(3)]
T = input()

print("".join(S[int(t) - 1] for t in T))
