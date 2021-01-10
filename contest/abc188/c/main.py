import numpy as np

N = int(input())
a = np.array(list(map(int, input().split())))

n = 2**N

first = np.argmax(a[:(n // 2)])
second = np.argmax(a[(n // 2):])

# print(f"{first=}, {(second)=}")

if a[first] > a[(n // 2):][second]:
    print(second + n // 2 + 1)
else:
    print(first + 1)
