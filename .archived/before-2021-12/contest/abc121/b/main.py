import numpy as np

N, M, C = map(int, input().split())
B = np.array(list(map(int, input().split())))
features = [list(map(int, input().split())) for _ in range(N)]
features = np.array(features)

calc = B * features
print(sum(calc.sum(axis=1) > -C))
