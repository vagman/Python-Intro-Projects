from textwrap import wrap
import re

filename = input("\nTest files you can use: test.txt\nEnter file to read: ")
try:
    f = open(filename, "r")
    data = f.read()
    
    result = ""
    for character in data:
        ascii_value = ord(character)

        # ASCII Functional character eg. space, tab, sound
        if ascii_value <= 32:
            result += " "

        # A-Za-z in ASCII
        elif ascii_value >= 65 and ascii_value <= 90 or ascii_value >= 97 and ascii_value <= 122:
            result += "A"

        # 0-9 digits
        elif re.match("[0-9]", character):     
            result += "1"
        
        # ASCII values < 128
        elif ascii_value < 128:
            result += "p"

        # nonASCII
        else:
            result += "?"

    # Print 16 characters/line
    print("\n".join(wrap(text = result, width = 16)))

    f.close()
except IOError:
    print("\nOops! The filename {} didn't match any of the files in this directory.\n".format(filename))