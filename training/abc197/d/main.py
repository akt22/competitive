import numpy as np

N = int(input())
x0, y0 = list(map(int, input().split()))
xn2, yn2 = list(map(int, input().split()))


def rotation(xy, r_axis, t):
    xy = np.array(xy)
    r_axis = np.array(r_axis)

    R = np.array([[np.cos(t), -np.sin(t)],
                  [np.sin(t), np.cos(t)]])

    return np.dot(R, xy - r_axis) + r_axis


xc, yc = (x0 + xn2) / 2., (y0 + yn2) / 2.
d = (2 * np.pi) / N
print(*rotation((x0, y0), (xc, yc), d))
