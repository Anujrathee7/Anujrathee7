file_name = input("Give the name of the CSV file:\n")

with open(file_name,'r+') as file:
    for line in file:
        list_char = line.split(",")
        new_list = []
        for char in list_char:
            new_list.append(char)
        ans = new_list[1].lstrip()
        print(ans)
