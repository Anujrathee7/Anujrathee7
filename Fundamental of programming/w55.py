def is_string_contained(substring, main_string):
    for i in range(len(main_string)):
        if main_string[i] == substring[0]:
            # Initialize a flag to check if the substring is found
            found = True
            # Iterate through the substring and main string
            for j in range(len(substring)):
                # If the characters don't match or if we've reached
                # the end of the main string, set the flag to False
                if i + j >= len(main_string) or main_string[i + j] != substring[j]:
                    found = False
                    break
            if found:
                return True

string1 = input("Enter the first string:\n")
string2 = input("Enter the second string:\n")
if (is_string_contained(string1,string2)):
    print("The first string can be found in the second string.")
else:
    print("The first string cannot be found in the second string.")
    
