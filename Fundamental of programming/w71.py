file_name = input("Enter the name of the file to be saved:\n")
with open(file_name,'w+') as file:
    while True:
        name = input("Enter a name or 'stop':\n")
        if(name != "stop"):
            file.write(name)
            file.write('\n')
        else:
            break
        
