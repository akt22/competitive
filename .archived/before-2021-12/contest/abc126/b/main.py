S = input()

first, second = int(S[:2]), int(S[2:])

if (1 <= first <= 12) and (1 <= second <= 12):
    print("AMBIGUOUS")
elif (first == 0 or first > 12) and (second == 0 or second > 12):
    print("NA")
elif (1 <= first <= 12) and (second == 0 or second > 12):
    print("MMYY")
else:
    print("YYMM")
