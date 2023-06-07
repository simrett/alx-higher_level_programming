#!/usr/bin/python3
def uppercase(string):
    for index in range(len(string)):
        character = ord(string[index])
        if character >= 97 and character <= 122:
            character = character - 32
        print("{}".format(chr(character)), end="")
    print()        
