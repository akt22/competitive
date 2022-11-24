import time

S = input()

print(time.strptime("Saturday", "%A").tm_wday - time.strptime(S, "%A").tm_wday)
