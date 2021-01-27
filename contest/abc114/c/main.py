N = int(input())


def base_10_to_n(X, n):
    if (int(X / n)):
        return base_10_to_n(int(X / n), n) + str(X % n)
    return str(X % n)


d = {"1": "3", "2": "5", "3": "7"}
seen = set()

ans = 0
for i in range(10, N):
    n = base_10_to_n(i, 4)
    if len(set(n) - set("0")) != 3:
        continue
    nn = int("".join([d[j] for j in n if j != "0"]))
    if nn in seen:
        continue
    elif nn > N:
        break
    else:
        seen.add(nn)
        ans += 1
print(ans)
