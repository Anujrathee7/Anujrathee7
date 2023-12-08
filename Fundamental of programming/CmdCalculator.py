# Python calculator

import sys

# total arguments
n = len(sys.argv)
if n != 4:
    print("Not a proper expression")
else:
    x = float(sys.argv[1])
    op = sys.argv[2]
    y = float(sys.argv[3])

    if op == "+":
        print(x + y)

    if op == "-":
        print(x - y)

    if op == "*":
        print(x * y)

    if op == ":":
        if y == 0:
            print("error")
        else:
            print(x / y)

