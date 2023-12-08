integer = int(input("Enter a positive integer:\n"))

if(integer <= 0 ):
    print(integer,"is not positive")
    exit(0)

i = int(1)
for i in range(1,integer +1):
    if(i%2 == 0):
        print(str(i),end='...')
        i= i+1