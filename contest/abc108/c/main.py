N, K = map(int, input().split())

# even = False
# if K % 2 == 0:
#     even = True

# o_cnt, e_cnt = 0, 0
# for i in range(1, N + 1):
#     if i % K == 0:
#         o_cnt += 1
#     if i % K == K // 2 and even:
#         e_cnt += 1
# print(o_cnt ** 3 + e_cnt ** 3)

num = [0] * N
for i in range(1, N):
    num[K % i] += 1

print(num)
ans = 0
for a in range(K):
    b = (K - a) % K
    c = (K - a) % K
    print(f"{a=}, {b=}, {c=}")
    if (b + c) % K == 0:
        ans += num[a] * num[b] * num[c]
print(ans)
