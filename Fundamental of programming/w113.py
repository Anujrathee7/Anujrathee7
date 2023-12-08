def sum(target,number_list):
    print("Pair with the sum of "+target)
    count = 1
    for num1 in number_list:
        for num2 in number_list[count:]:
            if(int(target) == int(num1)+int(num2)):
                if(int(num1)<=int(num2)):
                    print(f"({num1}, {num2})")
                else:
                    print(f"({num2}, {num1})")  
        count = count + 1


def main():
    number_list = []
    while True:
        number = input("Enter an integer (or type 'done' to finish input):\n")

        if(number=="done"):
            break
        else:
            number_list.append(int(number))
    
    target = input("Enter the target sum:\n")
    sum(target,number_list)


if __name__ == "__main__":
    main()