from datetime import date, timedelta

FILEPATH = "/Users/nickolasalcazar/Desktop/calendar2022.txt";

file = open(FILEPATH, "a")

start_day = 6
start_month = 6
start_year = 2022

end_day = 31
end_month = 12
end_year = 2022

start_date = date(start_year, start_month, start_day)
end_date = date(end_year, end_month, end_day)

delta = timedelta(days=1)		# Jump to next day

while start_date <= end_date:
    #print(start_date.strftime("%A, %m/%d"))
    file.write(start_date.strftime("%A, %-m/%-d\n"))

    start_date += delta

    if start_date.strftime("%w") == "0":
    	file.write("\n")
