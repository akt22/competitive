from datetime import datetime as dt

S = input()
if dt.strptime(S, "%Y/%m/%d") <= dt.strptime("2019/04/30", "%Y/%m/%d"):
    print("Heisei")
else:
    print("TBD")
