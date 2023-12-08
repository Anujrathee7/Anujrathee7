def main():
    try:
        first_number = input("Enter the first number:\n")
        second_number = input("Enter the second number:\n")
        print(f"The result of {float(first_number)} / {float(second_number)} is {round(float(first_number)/float(second_number),8)}")
    
    except ValueError:
        print("You must enter valid numbers")
    
    except ZeroDivisionError:
        print("You cannot divide by zero")

if __name__ == "__main__":
    main()