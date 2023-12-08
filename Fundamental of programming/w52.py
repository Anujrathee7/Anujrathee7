def count_words(string):
    total_words = int(1)
    for c in string:
        if(c == " "):
            total_words = total_words + int(1)
    print("This sentence contains",total_words,"words.")
    return 0 


string = input("Give a sentence:\n")
count_words(string) 