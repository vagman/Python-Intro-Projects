import requests
from collections import Counter

try:
    print("\nConnecting to ANU quantum computer...\n")
    response = requests.get('https://qrng.anu.edu.au/API/jsonI.php?length=1000&type=uint8')
    # The random numbers are returned in a JSON encoded array named ‘data’
    numbers = response.json()['data']

    # Modulo 20 every number
    result = []
    for numb in numbers:
        numb = numb % 20
        result.append(numb)
    
    data = Counter(result).most_common()

    # Number appearence frequency & statistics
    print("--- Statistics for 1000 given random numbers ---\n")
    for count, number_pair in enumerate(data):
        number = data[count][0]
        total_appearences = data[count][1]
        freq = str(total_appearences / len(result) * 100)
        print("Number {} appeared {} times which is {}%".format(number, total_appearences, freq[0:4]))

except requests.exceptions.RequestException as e:
    raise SystemExit(e)