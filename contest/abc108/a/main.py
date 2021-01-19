K = int(input())

odd = len(list(range(1, K + 1, 2)))
even = len(list(range(2, K + 1, 2)))
print(odd * even)
