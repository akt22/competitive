N = int(input())
names = [input() for _ in range(N)]

print("No" if len(names) == len(set(names)) else "Yes")
