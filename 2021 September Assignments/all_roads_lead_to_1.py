user_input = input("Enter a number: ")

try:
    numb = int(user_input)
    result = ""

    while not(numb == 1):
        # Fine numbers
        if numb % 2 == 0:
            numb = numb / 2
        
        # Prime numbers
        else:
            numb = numb * 3 + 1
        result = result + str(int(numb)) + " → "

    print("\n{} → {}\n".format(user_input, result[:-3]) )

except ValueError:
    print("\nOops! {} is not an integer. Please try again.\n".format(user_input))