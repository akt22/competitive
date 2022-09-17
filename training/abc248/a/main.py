S = input()

a = set([str(i) for i in range(0, 10)])

for i in a - set(list(S)):
    print(i)
