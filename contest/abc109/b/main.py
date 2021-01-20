N = int(input())
words = [input() for _ in range(N)]


vocab = []

prev = ""
for word in words:
    if prev == "":
        vocab.append(word)
        prev = word
        continue
    if prev[-1] == word[0] and word not in vocab:
        vocab.append(word)
        prev = word
    else:
        print("No")
        exit()
print("Yes")
