string = input("Enter a string:\n")
sum = int(0)

for variable in string:
    if(variable == 'a' or variable =='e' or variable =='i' or variable == 'o' or variable == 'u' or variable == 'A' or variable =='E' or variable =='I' or variable =='O' or variable =='U'):
        sum = sum + 1

print("Number of vowels is:",sum)