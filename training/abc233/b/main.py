L, R = list(map(int, input().split()))
S = input()

first = S[:L - 1]
second = S[R - 1:L - 2:-1] if L != 1 else S[R - 1::-1]
third = S[R:]
print(first + second + third)
