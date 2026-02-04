#👉 Filter only words with exactly 4 letters:

words = ["ball", "house", "sun", "table", "moon"]

words_4_letters = list(filter(lambda p: len(p) == 4, words ))
print(words_4_letters)
