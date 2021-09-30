import requests
import re 

try:
    print("\nConnecting to ANU quantum computer...\n")
    response = requests.get('https://qrng.anu.edu.au/API/jsonI.php?length=10&type=uint8')
    # The random numbers are returned in a JSON encoded array named ‘data’
    numbers = response.json()['data']

    print("Converting to 8-bit Binary...\n")
    binary = []
    for numb in numbers:
        binary.append("{0:08b}".format(numb))

    # Create lists of consecutive 0 & 1 so that we can iterate through
    zeros = []
    ones = []
    for bin in binary:
        print(bin)
        zeros.append(max(len(bin) for bin in re.findall(r'0+', bin)))
        ones.append(max(len(bin) for bin in re.findall(r'1+', bin)))

    print("\nMax number of consecutive zeroes appeared: {}.".format(max(zeros)))
    print("Max number of consecutive ones appeared: {}.\n".format(max(ones)))

except requests.exceptions.RequestException as e:
    raise SystemExit(e)