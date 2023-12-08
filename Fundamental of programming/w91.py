def employee_dictionary(dict_list):
    num_employees = int(input("How many employees do you want to add?:\n"))
    for i in range(num_employees):
        name = input("Enter worker's name:\n")
        workplace = input("Enter worker's workplace:\n")
        age = int(input("Enter worker's age:\n"))
        employee_info ={
            "name": name,
            "workplace": workplace,
            "age": age
        }
        dict_list.append(employee_info)

def print_info(dict_list):
    print("List of Employees:")
    for employee in dict_list:
        print(f"Name: {employee['name']}, Workplace: {employee['workplace']}, Age: {employee['age']}")

if __name__ == "__main__":
    empty_list = []
    employee_dictionary(empty_list)
    print_info(empty_list)

