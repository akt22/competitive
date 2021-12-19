A, B, C = map(int, input().split())

if A > B:
    print("Takahashi")
elif B > A:
    print("Aoki")
else:
    if C == 0:
        print("Aoki")
    else:
        print("Takahashi")
