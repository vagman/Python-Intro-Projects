from textwrap import wrap
import re

filename = input("\nTest files you can use: test.py, test,json, test.txt\nEnter file to read: ")
try:
    f = open(filename, "r")
    data = f.read()

    result_string = ""
    for character in data:
        # Functional character eg. {, +, /..
        if re.match("[^a-zA-Z1-9]", character):
            result_string += " "

        # A-Za-z
        elif re.match("[a-zA-Z]", character):
            result_string += "A"    

        # 0-9
        elif re.match("[0-9]", character): 
            result_string += "1"

        # 9-127
        elif int(character) > 9 and int(character) < 128:
            result_string += "p"

        else:
            result_string += "?"


    # Print 16 characters/line
    print("\n".join(wrap(text = result_string, width = 16)))
    
except IOError:
    print("\nOops! The filename {} didn't match any of the files in this directory.\n".format(filename))