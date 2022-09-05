N, M, X, T, D = list(map(int, input().split()))

if M >= X:
    print(T)
    exit()

init = T - (X * D)
print(init + (M * D))
