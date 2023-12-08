def main():
    number = input("Enter a number:\n")
    power(number)


def power(number):
    print("Powers of "+number+":")
    print("x^2:",round(pow(float(number),2),2))
    print("x^3:",round(pow(float(number),3),3))
    print("x^4:",round(pow(float(number),4),4))
    print("x^5:",round(pow(float(number),5),4))


if __name__ == "__main__":
    main()