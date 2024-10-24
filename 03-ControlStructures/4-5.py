###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    codes=[ord(char) for char in plain_text]
    # add one to the character's code
    encrypted_code=[code + 1 for code in codes]
    # replace new character code with its
    # corresponding character (use chr())
    encrypted_text=''.join([chr(code)for code in encrypted_code])
    # add encrypted character to encrypted text
    

print(f'{plain_text}')
print(f'{encrypted_text}')