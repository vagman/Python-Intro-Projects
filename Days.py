# Days Exercise 7

import datetime
from datetime import date

sum_day = 0
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

today = datetime.datetime.today()
today_str = int(today.strftime("%d")) # ex. 10
today_name = today.strftime("%A") # ex. Saturday
today_year = int(today.strftime("%Y")) # ex. 2018

for y in range(today_year + 1,today_year + 11):
	for m in range(1,13):
		if m == 12:
			days_of_month = date(y + 1, m - 11, 1) - date(y, m, 1)
		else:
			days_of_month = date(y, m + 1, 1) - date(y, m, 1)
		days_of_month = str(days_of_month)[0:2]
		
		for d in range(1,int(days_of_month) + 1):
			myDate = datetime.date(y,m,d)
			day = days[myDate.weekday()]
			if d == today_str: 
				if today_name == day:
					sum_day += 1

print("There will be {} {}s which will be the {}th, of the month, in the next 10 years.".format(sum_day , today_name, today_str))