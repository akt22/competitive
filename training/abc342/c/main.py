from string import ascii_lowercase

N = int(input())
S = input()
Q = int(input())

ops = ascii_lowercase

for _ in range(Q):
    c, d = input().split()
    ops = ops.replace(c, d)

print(S.translate(str.maketrans(ascii_lowercase, ops)))
