import datetime

def calendar(year,month):
    # finding the weekday for the first day of the month
    first_date = datetime.date(year,month,1)
    first_date_weekday = first_date.weekday()
    
    if(month == 12):
        next_month = datetime.date(year+1,1,1)
    else:
        next_month = datetime.date(year,month+1,1)
    
    day_in_month = (next_month - first_date).days

    print("_____________________\n Mo Tu We Th Fr Sa Su")
    print("   "*first_date_weekday,end="")
    for day in range(1,day_in_month+1):
        if((day+first_date_weekday)%7 == 0):
            print(f"{day:3}")    
        else:
            print(f"{day:3}", end="")

print("This program prints the calendar of a desired month.")
year = input("Give me the year:\n")
month = input("Give the month:\n")

calendar(int(year),int(month))
    
