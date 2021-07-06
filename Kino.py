# Kino Exercise 2

from urllib import request 
from urllib.request import urlopen
import json
import datetime

numb_list = []
numb = input("Give me 10 numbers seperated by commas: ")
numbs = numb.split(",")
for i in range(10):
	numb_list.append(int(numbs[i]))
	
success = []
days = []
cur_date = datetime.datetime.today()

for i in range(31):
	cur_date = cur_date - datetime.timedelta(days=1)
	date_str = cur_date.strftime("%d-%m-%Y")     
	url = "http://applications.opap.gr/DrawsRestServices/kino/drawDate/{}.json".format(date_str) 
	req = request(url)          
	response = urlopen(req)     
	data = response.read()              
	data = json.loads(data)               
	lottery = data["draws"]["draw"]      
	
	days.append(date_str)
	r = []
	success_sum = 0 # Counts the day's success rate

	for k in lottery:
		sum_4 = 0  # This is the sum that counts the 4 or more numbers
		lottery = k["results"]
		r.append(lottery)
		for j in range(0,10): # For every player's numb
			for numbers in range(0,20): # For every lottary's numb
				if numb_list[j] == 	lottery[numbers]: 
					sum_4 += 1
					if sum_4 > 4: # Found numbers > 4 , 5 found numbers = succ
						success_sum += 1
	success.append(success_sum)
	
# Here we sort 2 parallel lists so we can print the day with the most success rate !
for length in range(len(success) - 1, 0, -1):
	for i in range(length):
		if success[i] > success[i + 1]:
			temp1 = success[i]
			success[i] = success[i + 1]
			success[i + 1] = temp1
			# Sorting days list
			temp2 = days[i]
			days[i] = days[i + 1]
			days[i + 1] = temp2
x = success.index(max(success))

print("With the numbers you chose, your luckiest day is: ", days[x])