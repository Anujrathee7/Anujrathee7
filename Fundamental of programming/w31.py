year = int(input("Enter a year:\n"))
if((year%4)==0 and year != 1900):
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")
