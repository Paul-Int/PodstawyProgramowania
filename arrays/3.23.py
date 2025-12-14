import MyText

text = "An apple a day keeps the doctor away"

print("Text:", text)
print("Number of words:", MyText.word_count(text))

longest = MyText.words_longest_first(text)
print("Words from the longest:", end=" ")
for w in longest:
    print(w, end=", ")
print()

alphabetical = MyText.words_alphabetical(text)
print("Words ordered alphabetically:", end=" ")
for w in alphabetical:
    print(w, end=", ")
print()