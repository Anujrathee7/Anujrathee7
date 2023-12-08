file_name = input("Give the name of the input file:\n")
with open(file_name,'r+') as file:
    name_list= file.readlines()
    name_list.sort()
    for name in name_list:
        print(name,end="")