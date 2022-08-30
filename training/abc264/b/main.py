R, C = list(map(int, input().split()))

if R % 2 == 1 and C % 2 == 1:
    print('black')
elif R % 2 == 0 and C % 2 == 0:
    print('white')
elif R % 2 == 1 and C % 2 == 0:
    c = min(C, 15 - C)
    if c <= R <= 15 - c + 1:
        print('white')
    else:
        print('black')
else:
    r = min(R, 15 - R)
    if r <= C <= 15 - r + 1:
        print('white')
    else:
        print('black')
