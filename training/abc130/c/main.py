W, H, x, y = list(map(float, input().split()))

area = W * H / 2.

mx = W / 2.
my = H / 2.

flg = 0
if mx == x and my == y:
    flg = 1
print(area, flg)
