name = input("Enter a long word:\n")
print("The first five letters are:", name[0:5])
print("The last five letters are:",name[-5:])
print("Letters 2, 3, 4 and 5 are:",name[1:5])
print("Every second letter of the word:",name[1::2])
print("The word backwards \'"+name[-1::-1] +"\'")