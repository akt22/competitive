H, W = map(int, input().split())
h, w = map(int, input().split())

print(W * H - (H * w + W * h - h * w))
