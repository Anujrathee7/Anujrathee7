from datetime import datetime
date = input("Enter a date in YYYY-MM-DD format:\n")
format="%Y-%m-%d"
try:
    correctdate = datetime.strptime(date,format)
    print(date,"is a valid date.")
except:
    print(date,"is not a valid date.")