X1, X2, X3, X4 = list(map(int, list(input())))

if X1 == X2 == X3 == X4:
    print("Weak")
elif int(str(X1 + 1)[-1]) == X2 and int(str(X2 + 1)[-1]) == X3 and int(str(X3 + 1)[-1]) == X4:
    print("Weak")
else:
    print("Strong")
