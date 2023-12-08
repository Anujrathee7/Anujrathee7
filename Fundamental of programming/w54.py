def compressed(string):
    len1 = len(string)
    len2 = int(0)
    length = int(0)
    charac = string[0]
    total = int(0)
    print("Compressed string:",end=" ")
    for c in string:
        if(charac == c):
            total = total + int(1)
            length = length + 1
        else:
            if(total == 1):
                print(charac,end="")
                len2 = len2 + 1
            elif(total>10):
                print(charac+str(total),end="")
                len2 = len2 + 3
            else:
                 print(charac+str(total),end="")
                 len2 = len2 + 2

            charac = c
            length = length + 1
            total = int(1)
        if(length == len1):
            if(total == 1):
                print(charac,end="")
                len2 = len2 + 1
            elif(total>10):
                print(charac+str(total),end="")
                len2 = len2 + 3
            else:
                 print(charac+str(total),end="")
                 len2 = len2 + 2
    print("\nCompressing ratio",round(float(len2/len1),2))
    return 0 

compress = input("Give a string to compress:\n")
compressed(compress)
