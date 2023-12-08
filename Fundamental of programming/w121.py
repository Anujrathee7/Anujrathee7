def integer_sum(n: int):
    if(int(n) < 1):
        return n
    else:
        return n+integer_sum(n-2)




def main():
    integer = input("Give a non-negative integer n:\n")
    answer = integer_sum(int(integer))
    print("n + (n-2) + (n-4) + ... =",answer)

if __name__ == "__main__":
    main()