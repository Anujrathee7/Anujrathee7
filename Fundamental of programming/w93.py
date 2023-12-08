import json
# Load the data from the students.json file
with open('students.json', 'r') as file:
    student_data = json.load(file)
    print("Students who are 19 years old:")
    
    for data in student_data:
        if(int(data['age']) == 19):
            print(f"Student ID: {data['id']}, Name: {data['name']}, Age: {data['age']}")
    
    print("\nStudents whose name end with 'a':")
    for data in student_data:
        first_name = data['name'].split()[0]
        if(first_name.endswith('a')):
            print(f"Student ID: {data['id']}, Name: {data['name']}")


    print("\nStudents who study math:")
    for data in student_data:
        
        for subject in data['courses']:
            if(subject  == "Math"):
                print(f"Student ID: {data['id']}, Name: {data['name']}, Course: {data['courses']}")