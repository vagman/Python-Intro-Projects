from textwrap import wrap
import re

filename = input("\nTest files you can use: test.txt\nEnter file to read: ")
try:
    f = open(filename, "r")
    data = f.read()
    
    result_string = ""
    for character in data:
        ascii_value = ord(character)

        # ASCII Functional character eg. space, tab, sound
        if ascii_value <= 32:
            result_string += " "

        # A-Za-z in ASCII
        elif ascii_value >= 65 and ascii_value <= 90 or ascii_value >= 97 and ascii_value <= 122:
            result_string += "A"

        # 0-9 digits
        elif re.match("[0-9]", character):     
            result_string += "1"
        
        # ASCII values < 128
        elif ascii_value < 128:
            result_string += "p"
            
        else:
            result_string += "?"

    # Print 16 characters/line
    print("\n".join(wrap(text = result_string, width = 16)))

    f.close()
except IOError:
    print("\nOops! The filename {} didn't match any of the files in this directory.\n".format(filename))