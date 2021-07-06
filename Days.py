# Days Exercise 7

import datetime
from datetime import date

days_sum = 0
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

today = datetime.datetime.today()
current_date = int(today.strftime("%d")) # ex. 10
current_day = today.strftime("%A") # ex. Saturday
current_year = int(today.strftime("%Y")) # ex. 2018

def calculate_days(current_day, current_date, current_year, days_sum):
	for y in range(current_year + 1, current_year + 11):
		for m in range(1,13):
			if m == 12:
				days_of_month = date(y + 1, m - 11, 1) - date(y, m, 1)
			else:
				days_of_month = date(y, m + 1, 1) - date(y, m, 1)
			days_of_month = str(days_of_month)[0:2]

			for d in range(1,int(days_of_month) + 1):
				myDate = datetime.date(y,m,d)
				day = days[myDate.weekday()]
				if d == current_date: 
					if current_day == day:
						days_sum += 1
	print("There will be {} {}s which will be the {}th, of the month, in the next 10 years.".format(days_sum , current_day, current_date))

calculate_days(current_day, current_date, current_year, days_sum)