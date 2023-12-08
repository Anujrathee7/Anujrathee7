first = int(input("Enter a:\n"))
second = int(input("Enter b:\n"))
print("a:",first,"b:",second)

while (True):
    first = first * 2
    second = second + int(100)
    if(first > 1000):
        print("a exceeded 1000")
        if(second>1000):
            print("b exceeded 1000")
            exit(0)
        else:
            exit(0)
            
    else:
        print("a:",first,end=" ")

    if(second > 1000):
        print("b exceeded 1000")
        exit(0)
    else:
        print("b:",second)
