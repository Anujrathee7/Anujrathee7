def power(x: float,n: int):
    if(n < 1):
        return 1
    else:
        return x*power(x,n-1)


def main():
    x = float(input("Give a float x:\n"))
    n = int(input("Give a non-negative integer n:\n"))
    answer = power(x,n)
    print(f"{x} power to {n} is {answer}")

if __name__ == "__main__":
    main()