from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
questions = [list(map(int, input().split())) for _ in range(Q)]

acc = list(accumulate(A, initial=0))
for l, r in questions:
    win = acc[r] - acc[l - 1]
    total = r - l + 1
    lose = total - win
    if win > lose:
        print("win")
    elif win < lose:
        print("lose")
    else:
        print("draw")
