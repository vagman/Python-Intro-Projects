import requests
from re import findall

try:
    print("\nConnecting to ANU quantum computer...\n")
    response = requests.get('https://qrng.anu.edu.au/API/jsonI.php?length=1000&type=uint8')
    # The random numbers are returned in a JSON encoded array named ‘data’
    numbers = response.json()['data']

    print("Converting to 8-bit Binary...\n")
    binary = []
    for numb in numbers:
        binary.append("{0:08b}".format(numb))

    # Create lists of consecutive 0 & 1 digits so that we can iterate through to find max
    zeros = []
    ones = []
    for bin in binary:
        ones.append(max((len(bin) for bin in findall(r'1+', bin)), default=0))
        zeros.append(max((len(bin) for bin in findall(r'0+', bin)), default=0))

    print("\nMax count of consecutive zeroes appeared: {}.".format(max(zeros)))
    print("Max count of consecutive ones appeared: {}.\n".format(max(ones)))

except requests.exceptions.RequestException as e:
    raise SystemExit(e)