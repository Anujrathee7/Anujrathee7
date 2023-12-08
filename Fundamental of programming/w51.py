def occurences(ch,string):
    total = int(0)
    for c in string :
        if(c == ch):
            total = total + int(1)
    
    print("The character \'"+ch+"\' appears",total,"time(s) in the string.")
    return 0

    
ch = input("Enter a character:\n")
    
if(len(ch) != 1):
    print("Error: Give a single character.") 
    exit()
    
string = input("Enter a string:\n")
occurences(ch,string)



    
