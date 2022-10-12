text = "a b c a a b A B"

# text = """ Would you swear that you'll always be mine?
# Or would you lie?
# Would you run and hide? """


print(text.split())

word_count = {}

for word in text.lower().split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)