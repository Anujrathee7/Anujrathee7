while True:

    import math
    print("Trigonometric Calculations:")
    print("1. Sine Calculation\n2. Cosine Calculation\n3. Inverse Sine Calculation\n4. Inverse Cosine Calculation\n5. Exit")

    selection = input("Enter your choice (1/2/3/4/5):\n")
    if(int(selection) == 1):
        angle=input("Enter an angle in degrees:\n")
        radian=math.radians(float(angle))
        print("The sine of",float(angle),"degrees is",round(math.sin(radian),3),end="\n\n")

    elif(int(selection) == 2):
        angle=input("Enter an angle in degrees:\n")
        radian=math.radians(float(angle))
        print("The cosine of",float(angle),"degrees is",round(math.cos(radian),3),end="\n\n")

    elif(int(selection) == 3):
    
        value=input("Enter the sine value:\n")
        try:
            print("The inverse sine (in degrees) of",float(value),"is",round(math.degrees(math.asin(float(value))),3),end="\n\n")
        except:
            print("Invalid input. Sine value must be between -1 and 1.",end="\n\n")

    elif(int(selection) == 4):

        value=input("Enter the cosine value:\n")
        try:
            print("The inverse cosine (in degrees) of",float(value),"is",round(math.degrees(math.acos(float(value))),3),end="\n\n")
        except:
            print("Invalid input. Cosine value must be between -1 and 1.",end="\n\n")
    elif(int(selection) == 5):
        print("Bye!")
        break

    else:
        print("Invalid choice. Please select a valid option.",end="\n\n")