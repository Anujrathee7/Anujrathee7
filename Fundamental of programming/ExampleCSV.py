file_in = open("Example2.csv", "r")

M = []

lines = file_in.readlines() # read all lines
#print(lines) # list of strings ending with '\n'

for line in lines:
    line = line.strip("\n")  # This removes newline from the end
    line = line.split(",")   # This splits the line
    M.append(line)


# Prints the whole matrix (list of lists)
#print(M)   

# Print first row containing column names
#print(M[0]) 

# Print one firstname
#print(M[2][1])  

# Print all first names
for i in range(1,len(M)):
    print(M[i][1])


