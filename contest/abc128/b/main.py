N = int(input())

restaurants = []
for i in range(N):
    restaurant, score = input().split()
    score = int(score)
    restaurants.append([i + 1, restaurant, score])

restaurants.sort(key=lambda x: (x[1], -x[2]))

print(*[i[0] for i in restaurants], sep="\n")
