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

def print_matrix(matrix: list):
    count = 1
    for inner_list in matrix:
        print("|",end="")
        for num in inner_list:
            if(count == len(inner_list)):
                print(num,end="")
            else:
                print(num,end="	")
                count = count + 1
        print("|")
        count = 1

# Taking input for the numbers of rows and columns
row = input("Enter the number of rows:\n")
column = input("Enter the number of columns:\n")

# Calling the function to make a matrice
matrix = make_matrix(row,column)
print_matrix(matrix)
