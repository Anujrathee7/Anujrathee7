def reverse_string(s):
    if(len(s) <= 1):
        return s
    else:
        return  reverse_string(s[1:])+s[0]


def main():
    string = input("Give a string to reverse:\n")
    reverse = reverse_string(string)
    print(f"Original String: {string}")
    print(f"Reversed String: {reverse}")

if __name__ == "__main__":
    main()