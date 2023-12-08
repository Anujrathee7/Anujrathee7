from datetime import datetime,timedelta
date1 = input("Enter the first date (DD.MM.YYYY):\n")
date2 = input("Enter the second date (DD.MM.YYYY):\n")
format = "%d.%m.%Y"
date1format = datetime.strptime(date1,format)
date2format = datetime.strptime(date2,format)
diff = date2format-date1format
if(int(diff.days) < 0):
    diff = date1format-date2format
    print("The number of days between",date1,"and",date2,"is",diff.days,"days.")

else:
    print("The number of days between",date1,"and",date2,"is",diff.days,"days.")