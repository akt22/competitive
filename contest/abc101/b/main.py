N = int(input())

sn = sum(map(int, list(str(N))))

print("Yes") if N % sn == 0 else print("No")
