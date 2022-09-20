A, B, C, D = list(map(int, input().split()))

if A > C:
    print("Aoki")
else:
    if A == C:
        if B > D:
            print("Aoki")
        else:
            print("Takahashi")
    else:
        print("Takahashi")
