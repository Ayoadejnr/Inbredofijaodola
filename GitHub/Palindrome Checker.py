word = input('Enter a word: ').lower()
palindrome = str(word[::-1])
if word == palindrome:
    print("Word is a palindrome")
else:
    print('Word is not a palindrome')