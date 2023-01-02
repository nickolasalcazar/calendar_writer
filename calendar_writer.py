from datetime import date, timedelta

OUTPUT_PATH = "/Users/nickolasalcazar/Desktop/calendar2023.txt";

file = open(OUTPUT_PATH, "a")

start_day = 1
start_month = 1
start_year = 2023

end_day = 31
end_month = 12
end_year = 2023

start_date = date(start_year, start_month, start_day)
end_date = date(end_year, end_month, end_day)

delta = timedelta(days=1)		# Jump to next day

while start_date <= end_date:
    #print(start_date.strftime("%A, %m/%d"))
    file.write(start_date.strftime("%A, %-m/%-d\n"))

    start_date += delta

    if start_date.strftime("%w") == "0":
    	file.write("\n")
