from read_file import ReadingTxtFile
import re
from collections import Counter

r = ReadingTxtFile()

try:
    filename = input("\nEnter an ASCII text file. Sample filename 'input'\n")
    data = r.read_txt(filename)
    print("\nPrinting letter statistics...\n")

    # Conver to int in order to find prime numbers
    ascii_values = []
    for character in data:
        ascii_values.append(int(ord(character)))

    # Create list in order to iterate over it
    primes = []
    for value in ascii_values:
        if value % 2 != 0:
            primes.append(value)

    # Convert back to ASCII in order to calculate statistics
    for count, ascii_code in enumerate(primes):
        primes[count] = chr(ascii_code)

    # Remove unwanted characters like "'"
    regex = re.compile('[a-zA-Z]')
    ascii_prime_letters =list(filter(regex.match, primes))

    # Extract how many time a letter appeared e.g. ('e', 59) & calculate % list(tuple1, tuple2, ..)
    data = Counter(ascii_prime_letters).most_common()
    for count, character in enumerate(data):
        letter_freq = str(data[int(count)][1]/len(ascii_prime_letters) * 100)

        # Differentiate 21.6% from 9.15% depending on the decimal point
        if "." == letter_freq[2]:
            asterisks = int(letter_freq[0:2]) + 1
            print("{} appeared {} ({}%) times: {}".format(data[int(count)][0], data[int(count)][1], letter_freq[0:3], "*" * asterisks))
        else:
            asterisks = int(letter_freq[0]) + 1
            print("{} appeared {} ({}%) times: {}".format(data[int(count)][0], data[int(count)][1], letter_freq[0:3], "*" * asterisks))

except IOError:
    print("\nOops! The filename {} didn't match any of the files in this directory.\n".format(filename))