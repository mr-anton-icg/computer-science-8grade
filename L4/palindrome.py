# check palindrome

word = 'madam'
word_backward = ''
for x in word:
    word_backward = x + word_backward

if word == word_backward:
    print(f'word `{word}` is palindrome')
else:
    print(f'word `{word}` is NOT palindrome')