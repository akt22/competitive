V, A, B, C = list(map(int, input().split()))

d = A + B + C
remain = V % d

if remain < A:
    print("F")
elif remain < A + B:
    print("M")
else:
    print("T")
