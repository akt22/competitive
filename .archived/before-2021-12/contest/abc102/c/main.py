from statistics import median

N = int(input())
a = map(int, input().split())

l = []
for idx, _a in enumerate(a):
    b = _a - (idx + 1)
    l.append(b)

med = median(l)
print(int(sum([abs(b - med) for b in l])))
