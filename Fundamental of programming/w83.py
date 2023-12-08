from datetime import datetime

time = input("Give a datetime string in format \"%Y/%m/%d %H:%M:%S\":\n")
date = datetime.strptime(time,'%Y/%m/%d %H:%M:%S')
month = date.strftime('%B')
weekdays= date.strftime('%A')
week = date.strftime('%W')
day = date.strftime('%j')
print("Month:",month)
print("Weekday:",weekdays)
print("Week nr:",week)
print("Day nr:",day)