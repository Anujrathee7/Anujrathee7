#Taking input from the user
name = input("Give a word:\n")
#Printing the length of the string
print("The length of the word is",len(name))
#Taking the input to replace a letter from the string
index = int(input("Give an integer smaller than or equal to " + str(len(name)) + ":\n"))
index = index - 1
#Printing the answer
First = name[0:index]
last = name [index+1:]
print(First + "*" + last)

