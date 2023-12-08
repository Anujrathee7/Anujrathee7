import numpy as np

def main():
    matrix_one = matrix("first")
    print("This is matrix 1:")
    print(matrix_one)
    matrix_two = matrix("second")
    print("This is matrix 2:")
    print(matrix_two)
    sum(matrix_one,matrix_two)
    multiply(matrix_one,matrix_two)


def matrix(number):
    row = input(f"Enter the number of rows for the {number} matrix:\n")
    column = input(f"Enter the number of columns for the {number} matrix:\n")
    print(f"Enter values for a {row}x{column} matrix:") 
    matrix = []
    for num in range(int(row)):
        elements = []
        column_element = input(f"Enter {column} values for row {num+1} (separated by space):\n")
        colum_list = column_element.split()
        for char in colum_list:
            elements.append(float(char))
        
        matrix.append(elements)
    numpy_matrix = np.array(matrix)
    return numpy_matrix


def sum(matrix_one,matrix_two):
    if(np.shape(matrix_one) != np.shape(matrix_two)):
        print("Error: sum not possible")
    else:
        sum = matrix_one + matrix_two
        print("Matrix sum:")
        print(sum)

def multiply(matrix_one,matrix_two):
    try:
        result = np.dot(matrix_one,matrix_two)
        print("Matrix multiplication:")
        print(result)
    except:
        print("Error: multiplication not possible")
    
if __name__ == "__main__":
    main()