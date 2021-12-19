cards = list(map(int, input().split()))

cards.sort(reverse=True)

print(cards[0] * 10 + cards[1] + cards[2])
