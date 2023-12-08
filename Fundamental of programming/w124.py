def gcd(a,b):
    if(b == 0):
        return a
    else:
        return gcd(b,a%b)


def main():
    integer = input("Give two positive integers separated by comma:\n")
    integer_list = integer.split(",")
    a = int(integer_list[0])
    b = int(integer_list[1])
    answer = gcd(a,b)
    print(f"gcd({a},{b}) = {answer}")

if __name__ == "__main__":
    main()