def sum(count):
    total_sum = 0
    number = 0
    print(f"Now give {count} integers!")
    while(number<int(count)):
        try:
            integer = input("Enter an integer:\n")
            total_sum = total_sum + int(integer)
            number = number + 1
        except:
            print("Invalid input. Please enter an integer.")
    print(f"The sum of the entered integers is: {total_sum}")


def main():
    while True:
        try:
            count = int(input("Enter an integer:\n"))
            sum(count)
            break
        except:
            print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()