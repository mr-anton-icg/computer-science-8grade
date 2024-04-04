# drop sequential duplicated symbols

word = 'Odesssssssa'
word_new = ''
prev_x = ''
for x in word:
    if x != prev_x:
        prev_x = x
        word_new = word_new + x # word_new += x

print(word)
print(word_new)