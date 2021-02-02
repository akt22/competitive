N, M = map(int, input().split())

answers = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]

cnt = [0] * M
for answer in answers:
    for food in answer[1:]:
        cnt[food] += 1
print(sum([c == N for c in cnt]))
