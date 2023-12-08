#########################################################################
# CT60A0203 Introduction to Programming - Online teaching
# Name:Anuj Rathee
# Student number:001715080
# Email:Anuj.Rathee@student.lut.fi
# Date:29 November 2023
# By submitting this work, I certify that i have written the code by myself.
#
# 
#
#########################################################################


                                                     ## Starting of the adding student function #

import csv

def add_student():
    import random
    from datetime import datetime
    # Loop used to take input until valid name is given
    
    while True:
     
        print(f"Names should contain only letters and start with capital letters.")
        first_name = input(f"Enter the first name of the student:\n")
        last_name = input(f"Enter the last name of the student:\n")
    
    # Checking if the name given by user is valid or not
    
        if(valid_name(first_name) and valid_name(last_name)):
            break
    
    # Creating email for the student using the eamil format and the year of enrolment
    
    student_email = generate_email(first_name,last_name)
    
    year = datetime.now().year
    
    # Generating a random ID for the student
    while True:
        flag = True
        student_id =  random.randrange(10001,99998)
        with open('students.txt','r+') as file:        
            field = ['id']
            information = csv.DictReader(file, fieldnames=field)

            for list_information in information:
           # Generating a list from line to check the ID
                if(int(student_id) == int(list_information['id'])):
                    flag = False
                    break
        
        if(flag):
            break

    # Selecting major for the student
    
    while True:
        print("""Select student's major:
                                 CE: Computational Engineering
                                 EE: Electrical Engineering
                                 ET: Energy Technology
                                 ME: Mechanical Engineering
                                 SE: Software Engineering""")
        major = input("What is your selction?\n")
    
        if(major == "CE" or major == "EE" or major == "SE" or major == "ME" or major == "ET"):
            break

    complete_information = str(student_id) + ',' + first_name + ',' + last_name + ',' + str(year) + ',' + major + ',' + student_email


    with open('students.txt','a') as file:
        file.write(complete_information+"\n")
    print("Student Added successfully!")
    return
    
# Checking if the name is valid or not

def valid_name(name):

    if(name.isalpha() == False):
        return False

    count = int(0)

    for char in name:

        if(char.isdigit()):
            return False

        elif(char.islower() and count == 0):
            return False

        elif(count > 0  and char.isupper()):
            return False

        count = count + 1

    return True
    
                                        ## Ending of the adding student function ##





def generate_email(first_name,last_name):
    email = first_name.lower()+'.'+last_name.lower()+'@lut.fi'
    return email    



                                        ## Starting of search student function ##

def search_student():
    
    while True:
        name = input("Give at least 3 characters of the students first or last name:\n")
    
        if len(name) >= 3 and not " " in name:
            break 

    
    # Getting student information from the give characters of the student name

    print("Matching students:")

    with open('students.txt','r') as file:

        field = ['id', 'first_name', 'last_name', 'starting_year', 'major', 'email']
        information = csv.DictReader(file, fieldnames=field)
        
        for student_information in information:

            if(name in student_information['first_name']):
                print("ID: "+student_information['id']+", First name: "+ student_information['first_name']+", Last name: "+student_information['last_name'])
           
            elif(name in student_information['last_name']):
                print("ID: "+student_information['id']+", First name: "+ student_information['first_name']+", Last name: "+student_information['last_name'])



                                                ## Ending of the search student function ##







                                                ## Starting of the search course function ##

def search_course():
    import csv
    while True:
        name = input("Give at least 3 characters of the name of the course or the teacher:\n")
    
        if len(name.replace(" ", "")) >= 3:
            break

    # Opening file courses.txt in read mode to check the courses

    with open('courses.txt','r') as file:

        for lines in file:
           
            course_inforamtion = lines.split(",")
            teacher_name = course_inforamtion[3:]
           
           # Checking if the course name contains the given characters
           
            if(name in course_inforamtion[1]):
                print("ID: "+course_inforamtion[0]+", Name: "+course_inforamtion[1]+", Teacher(s): "+", ".join(teacher_name),end="")
           
            # If course name does not contain the charactes then checking in teachers Name 
                      
            else:     
                for teacher in teacher_name:
                   
                    if(name in teacher):
                        print("ID: "+course_inforamtion[0]+", Name: ",course_inforamtion[1],", Teacher(s): ",", ".join(teacher_name),end="")
                        break




                                                ## Ending of the search course function ##                            




                                                ## Starting of the Add course completion function ##

def add_course():
    import datetime
    import csv  # Add the import statement for the csv module

# Getting course ID from the user
    while True:
        condition = False
        course_id = input("Give the course ID:\n")
    
        with open('courses.txt', 'r') as file:
            course_field = ['course_id', 'name', 'credit', 'student_name']
            information = csv.DictReader(file, fieldnames=course_field)

            # Loop through each row in the file
            for row in information:
                if row['course_id'] == course_id:
                    condition = True
                    break  # Exit the loop if the course ID is found
        
        if condition:
            break

    
    # Getting student ID from the user
    while True:
        student_id = input("Give the student ID:\n")
        if(student_exist(student_id)):
            break

    
    # Getting grade from the user
    grade = input("Give the grade:\n")
    try:   
        if(int(grade) < 0 or int(grade) > 5):
            print("Grade is not a correct grade")
            return
    
    except:
        print("Grade is not a correct grade.")
        return
    
    # Comparing with the previous grade if present

    with open('passed.txt','r') as file:

        field = ['id', 'student_id', 'date', 'grade']

        passed_information = csv.DictReader(file, fieldnames=field)
            
        for information in passed_information:

            if(information['id'] == course_id and information['student_id'] == student_id):  

                if(int(grade) <= int(information['grade'])):
                    print(f"Student has passed this course earlier with grade {information['grade']}")
                    return


    # Getting Date from the user
    date = input("Enter a date (DD/MM/YYYY):\n") 
        
    if(val_date(date) == False):
        print("Invalid date format. Use DD/MM/YYYY. Try again!")
        return
    
    

    # Stripping date from the string given by the user to datetime format

    completion_date = datetime.datetime.strptime(date,'%d/%m/%Y')
    today = datetime.datetime.today()
    difference = today - completion_date
    
    
    if(int(difference.days)>30):
        
        print("Input date is older than 30 days. Contact \"opinto\".")
        return

    elif(int(difference.days) < 0):
        
        print("Input date is later than today. Try again!")
        return
    
    else:
        print("Input date is valid.")

    
    if(new_passed_student(course_id,student_id,date,grade)):
        print("Record added!")
        return
    
    else:
        with open('passed.txt','r') as file:
        
            all_lines = file.readlines()
            count = 0
            
            for line in all_lines:
                information = line.split(",")
                if(information[0] == course_id and information[1] == student_id):
                    all_lines[count] = passing_information = course_id + "," + student_id + "," + date + "," + grade + "\n"
                else:
                    count = count + 1
    
        with open('passed.txt','w') as file:
            
            for line in all_lines:
                file.write(line)
            
            print("Record added!")



                                                            ## End of the add course completion function ##

                                ## Sub funtion for the add completion function ##




def student_exist(id):
    with open('students.txt','r') as file:
        field = ['id', 'first_name', 'last_name', 'starting_year', 'major', 'email']
        information = csv.DictReader(file, fieldnames=field)

        for student_id in information:
            if(id == student_id['id']):
                return True

    return False


def val_date(input):
    from datetime import datetime
    try:
        dateobject = datetime.strptime(input,'%d/%m/%Y')
        return True
    except:
        return False


def new_passed_student(course_id,student_id,date,grade):
    
    with open('passed.txt','r') as file:            
        
        field = ['id', 'student_id', 'date', 'grade']

        passed_information = csv.DictReader(file, fieldnames=field)

        for information in passed_information:
            
            if(information['id'] == course_id and information['student_id'] == student_id):
                return False
    
    
    with open('passed.txt','a') as file:

        passing_information = course_id + "," + student_id + "," + date + "," + grade
        file.write(passing_information+"\n")
        return True




                                        ## End of the sub functions ##

                                        ####### Starting of the student record function ######


def get_major_name(major_code):
    # Map major codes to their respective names
    majors = {
        "CE": "Computational Engineering",
        "EE": "Electrical Engineering",
        "ET": "Energy Technology",
        "ME": "Mechanical Engineering",
        "SE": "Software Engineering"
    }
    return majors.get(major_code)



def student_record():
    
    student_id = input("Student ID: ")
    found_student = False
    
    
    with open('students.txt', 'r') as students_file:
        field_names = ['id', 'first_name', 'last_name', 'starting_year', 'major', 'email']
        students_info = csv.DictReader(students_file, fieldnames=field_names)
        
        
        for student_info in students_info:
           
            if student_id == student_info['id']:
                print(f"Name: {student_info['last_name']}, {student_info['first_name']}")
                print(f"Starting year: {student_info['starting_year']}")
                print(f"Major: {get_major_name(student_info['major'])}")
                print(f"Email: {student_info['email']}")
                found_student = True
                break
    
    if not found_student:
        print("Invalid ID!")
        return
    
    print("\nPassed Courses:\n")
    total_credits = 0
    total_grade = 0
    course_count = 0

    with open('passed.txt', 'r') as passed_file:
        for line in passed_file:
            course_info = line.split(",")
            if student_id == course_info[1]:
                course_id = course_info[0]

                with open('courses.txt', 'r') as courses_file:
                    
                    courses_info = csv.reader(courses_file)
                    
                    for course_row in courses_info:
                    
                        if course_row[0] == course_id:
                    
                            teacher_name = ", ".join(course_row[3:]).strip('\n')
                    
                            print(f"Course ID: {course_row[0]}, Name: {course_row[1]}, Credits: {course_row[2]}")
                            print(f"Date: {course_info[2]}, Teacher(s): {teacher_name}, Grade: {course_info[3]}")

                            total_credits += int(course_row[2])
                            total_grade += int(course_info[3])
                            course_count += 1
                    
                            break

    print(f"Total credits: {total_credits}, ", end="")
    if course_count == 0:
        print(f"Average grade: 0.0")
    else:
        print(f"Average grade: {round(float(total_grade / course_count), 1)}")




#  Creating the menue for the operation

def main():
    while True:

        print("""You may select one of the following:
               1) Add student
               2) Search student
               3) Search course
               4) Add course completion
               5) Show student's record
               0) Exit""")

        try:
            operation = input("What is your selection?\n")
        
        
            if(int(operation) == 0):
                break

            elif(int(operation) == 1):
                add_student()

            elif(int(operation) == 2):
                search_student()

            elif(int(operation) == 3):
                search_course()

            elif(int(operation) == 4):
                add_course()
    
            elif(int(operation) == 5):
                student_record()
        
        except:
            print("Incorrect Input")



if __name__ == "__main__":
    main()