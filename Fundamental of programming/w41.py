integer = int(input("Enter a non-negative integer:\n"))

if(integer < 0 ):
    print("Error: Factorial is not defined for negative numbers")
    exit(0)
    
factorial = 1
i = 1
for i in range(1,integer+1):
    factorial = factorial * i   
    i=i+1

print("Factorial of",integer,"is",factorial)

    