import sys

try: 
        with open(sys.argv[1],"r") as file:
            print(f"Contents of {sys.argv[1]}:")
            for line in file:
                print(line,end="")
except:
    try:
        if(sys.argv[1]):
            if(sys.argv[1] == "story.txt"):
                print("Usage: python read_file.py <filename>")
            else:    
                print(f"Error: File '{sys.argv[1]}' does not exist.")
    except:
        print("Usage: python read_file.py <filename>")