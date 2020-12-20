N = int(input().strip())
problems = list(map(int, input().strip().split(" ")))

pattern = set([0])
for p in problems:
    for tmp in list(pattern):
        pattern.add(tmp + p)
print(len(pattern))
