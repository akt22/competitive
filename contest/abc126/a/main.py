N, K = list(map(int, input().split()))
S = input()

print(f"{S[:K-1]}{S[K-1].lower()}{S[K:]}")
