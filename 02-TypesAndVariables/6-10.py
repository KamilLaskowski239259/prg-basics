###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
a=movie.upper()
print(a)

# print title in small letters
a=movie.lower()
print(a)

# print how many times the vowel "e" appears in the title
a=movie.count('e')
print(a)
# print where in the text is the word "Lord"
a=movie.rfind('Lord')
print(a)

# print where in the text is the word "dragon"
...