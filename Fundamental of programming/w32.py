answer = input("Do you want to stop the execution of the program (y/Y):\n")
if(answer == 'Y' or answer == 'y'):
    print("Bye!")
    exit(0)

else:
    name = input("Enter username:\n")
    password = input("Enter password:\n")

if(name == 'Mark' and password == 'drowssap'):
    print("User recognized.")
else:
    print("You entered an invalid login name or password.")
