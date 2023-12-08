first_number =float(input('''This program calculates the average of the 3 numbers you enter.\nThe numbers can be int's or float's\nEnter the first number:\n'''))

second_number = float(input("Enter the second number:\n"))

third_number = float(input("Enter the third number:\n"))

#Sum of the 3 numbers 
sum1 = float(first_number) + float(second_number) + float(third_number)
intsum = int(first_number)+ int(second_number) + int(third_number)
print("Sum of the numbers:",round(sum1,3))

#Average of the numbers
print("Average of the numbers (rounded to 3 decimal places):",round(sum1/3,3))
print("Average of the numbers (rounded to the closest integer):",round(sum1/3))
print("Average of the numbers as an integer without the decimal part:",round(intsum/3))
