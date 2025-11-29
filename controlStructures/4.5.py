###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # check if the character is a letter
    if char.isalpha():
        code = ord(char)          # read the character's code
        code += 1                 # add one to the character's code
        
        new_char = chr(code)      # convert the code back to a character
        encrypted_text += new_char
    else:
        # keep spaces and punctuation unchanged
        encrypted_text += char

print(plain_text)
print(encrypted_text)