file_name = input("Give the text file to analyze:\n")

with open(file_name,'r+') as file:
    line_count = int(0)
    word_count  = int()
    for line in file:
        word_count = word_count + 1
        line_count = line_count + 1
        for word in line:
            if(word == " "):
                word_count = word_count + 1
        
            
    
    print("Number of lines:",line_count)
    print("Number of words:",word_count)