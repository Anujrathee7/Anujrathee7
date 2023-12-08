#Defining the function to make a matrice
def make_matrix(row,column):
    n = int(1)
    matrix = []
    # Loop to take input for each row
    while n<=int(row):
        # Taking input for the row to make a list
        int_input = input("Give row "+str(n)+":\n")
        int_char = int_input.split()
        int_list = []
        
        #Making the list for the matrice
        for ch in int_char:
            int_list.append(int(ch))
        
        #Checking whether the number of row match with the input
        if(int(len(int_list)) == int(column)):
            matrix.append(int_list)
            n = n+1
        else:
            print("Error: Invalid number of elements in the row. Please try again.")
    return matrix

#Function to print the transpose
def print_transpose(matrix: list,row,column):
    
    for column_count in range (0,int(column)):
        print("|",end="")
    
        for row_count in range(0,int(row)):
    
            if(row_count == int(row)-1):
                print(matrix[row_count][column_count],end="")
            else:
                print(matrix[row_count][column_count],end="	")
    
        print("|")




#Function to print the matrix
def print_matrix(matrix: list):
    count = int(1)
    for sub_list in matrix:
    
        print("|",end="")
    
        for integer in sub_list:
            if(count == len(sub_list)):
                print(integer,end="")
            else:
                print(integer,end="	")
                count = count+1
    
        print("|")
        count = int(1)
        
            



#Taking number of rows and column to make a matrix
row = int(input("Enter the number of rows:\n"))
column = int(input("Enter the number of columns:\n"))

matrix = make_matrix(row,column)
print("The original matrix:")
print_matrix(matrix)
print("Its transpose:")
print_transpose(matrix,row,column)