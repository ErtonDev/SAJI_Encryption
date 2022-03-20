# Modules
import string
import io
from pathlib import Path

# User's path so that the program is compatible on other computers
client_path = Path(__file__)

# Characters that can be encrypted and decrypted are stored here for later
alphabet = string.ascii_lowercase
char_list = list(alphabet)


# Clean memory file
def clean_memory():
    cleaning = io.open((client_path / '../memory_file.txt').resolve(), 'w')
    cleaning.write('')
    cleaning.close()


# Functions for S.A.J.I. encryption
def encryption(text):
    # First cleans memory
    clean_memory()

    # Text goes through a loop where every character is identified and swapped by a different one
    for char in text:
        # Checks if the character can be encrypted
        if char in char_list:

            # Loop determines the swapping characters
            for i in char_list:
                if char == i:
                    i_location = char_list.index(i)

                    # Uses the location of i to determine what that length +2 would be
                    # That value will determine the character that char will be swapped for
                    # But last two chars in char_list generate some issues because their locations +2 are out of index
                    # So those last two characters get a special condition
                    if char == char_list[24]:
                        # Y letter
                        new_location = 0
                        # So it would be A
                    elif char == char_list[25]:
                        # Z letter
                        new_location = 1
                        # So it would be B
                    else:
                        new_location = i_location + 2

                    # Finally write down in the memory file the swapped character
                    memory_file = io.open((client_path / '../memory_file.txt').resolve(), 'a')
                    memory_file.write(char_list[new_location])
                    memory_file.close()

        else:
            # Character doesn't need to be encrypted so it will be written in the memory file without being swapped
            memory_file = io.open((client_path / '../memory_file.txt').resolve(), 'a')
            memory_file.write(char)
            memory_file.close()

    # Once it is done...
    open_memory = io.open((client_path / '../memory_file.txt').resolve(), 'r')
    result = open_memory.read()
    open_memory.close()

    return result


def decryption(text):
    # First cleans memory
    clean_memory()

    # Text goes through a loop where every character is identified and swapped by the original one
    for char in text:
        if char in char_list:

            # Most stuff here is like the encryption function
            for i in char_list:
                if char == i:
                    i_location = char_list.index(i)

                    # Uses the location of i to determine what that length -2 would be
                    # That value will determine the original character
                    # But first two chars in char_list generate some issues because their locations -2 are out of index
                    # So those first two characters get a special condition
                    if char == char_list[0]:
                        # A letter
                        new_location = 24
                        # So it would be Y
                    elif char == char_list[1]:
                        # B letter
                        new_location = 25
                        # So it would be Z
                    else:
                        new_location = i_location - 2

                    # Finally write down in the memory file the swapped character
                    memory_file = io.open((client_path / '../memory_file.txt').resolve(), 'a')
                    memory_file.write(char_list[new_location])
                    memory_file.close()

        else:
            # Character doesn't need to be decrypted so it will be written in the memory file without being swapped
            memory_file = io.open((client_path / '../memory_file.txt').resolve(), 'a')
            memory_file.write(char)
            memory_file.close()

    # Once it is done...
    open_memory = io.open((client_path / '../memory_file.txt').resolve(), 'r')
    result = open_memory.read()
    open_memory.close()

    return result


'''
if __name__ == '__main__':
    user_input = input(str('Text: '))

    print('ENC:')
    enc_text = encryption(user_input)
    print(enc_text)

    print('DEC:')
    print(decryption(enc_text))
'''
