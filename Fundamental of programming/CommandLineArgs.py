# Python program to demonstrate
# command line arguments

import sys

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

# Arguments passed
print("Name of Python script:", sys.argv[0])

# Print the arguments
print("Arguments passed:", end = " ")

for i in range(1, n-1):
    print(sys.argv[i], end = ", ")
print(sys.argv[n-1])
