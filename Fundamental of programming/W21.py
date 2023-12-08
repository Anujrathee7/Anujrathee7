import math
#Taking input from the user
name = input("Enter your name:\n")
integer = int(input("Enter an integer:\n"))
number = float(input("Enter a float:\n"))
#Printing the answer
print("Decimal",number,"to power",integer,"is",round(float(pow(number,integer)),2))
print("Thank you for using the program",name +"!")
