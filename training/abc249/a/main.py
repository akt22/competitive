A, B, C, D, E, F, X = list(map(int, input().split()))

t1 = X // (A + C)
t2 = X % (A + C)
t = ((t1 * A) + min(t2, A)) * B

a1 = X // (D + F)
a2 = X % (D + F)
a = ((a1 * D) + min(a2, D)) * E

print("Takahashi" if t > a else "Aoki" if t < a else "Draw")
