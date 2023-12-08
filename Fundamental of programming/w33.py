first_number = int(input("Enter the first number:\n"))
second_number = int(input("Enter the second number:\n"))
print("The calculator can perform the following operations:\n1) Add\n2) Subtract\n3) Multiply \n4) Divide")
print("The numbers you entered are", first_number,"and",second_number)
operation = int(input("Select the operation (1-4):\n"))
if(operation == 1):
    print("Selection 1:",first_number,"+",second_number,"=",int(first_number+second_number))
elif(operation == 2):
        print("Selection 2:",first_number,"-",second_number,"=",int(first_number-second_number))
elif(operation == 3):
        print("Selection 3:",first_number,"*",second_number,"=",int(first_number*second_number))
elif(operation ==4 and second_number != 0):
        print("Selection 4:",first_number,"/",second_number,"=",round(float(first_number/second_number),2))
elif(operation ==4 and second_number == 0):
            print("Error: Zero cannot be used as a divisor.")
else:
                print("The operation was not recognized.")