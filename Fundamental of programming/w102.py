def main():
    file_name = input("Enter the file name:\n")
    try:
        with open(file_name,'r') as file:
            print("File content:")
            for line in file:
                print(line,end="")
    
    except:
        print("Error: File not found.")

if __name__ == "__main__":
    main()