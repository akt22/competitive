S1 = input()
S2 = input()
S3 = input()

S_all = set(["ABC", "ARC", "AGC", "AHC"])
S = set([S1, S2, S3])
print(list(S_all - S)[0])
