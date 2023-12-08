def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    try:
        row = int(input("Enter the row index:\n"))
        column = int(input("Enter the column index:\n"))
        print(f"Value at position ({row}, {column}): {matrix[row][column]}") 
    except ValueError:
        print("Error: Please enter valid integers for row and column indices.")
    except IndexError:
        print("Error: Index out of bounds. Please enter valid row and column indices.")

if __name__ == "__main__":
    main()