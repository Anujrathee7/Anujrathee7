first = input("Enter word 1:\n")
second = input("Enter word 2:\n")
len1 = int(len(first))
len2 = int(len(second))
n = int(0)
if(first == second):
    print("The words are the same.")

while n < len1 :
    if(ord(first[n]) > ord(second[n])):
        print("\'"+ second +"\' comes earlier in order than \'"+ first + "\'.")
        break
    
    elif(ord(first[n]) < ord(second[n])):
        print("\'"+ first +"\' comes earlier in order than \'"+ second + "\'.")
        break
    else:
        n=n+1

if('z' in first):
    print("Letter 'z' is found in word \'"+ first + "\'.")
if('z' in second):
    print("Letter 'z' is found in word \'"+ second + "\'.")
else:
    print("The letter 'z' was not found in either of the words.")

palindrome = input("Enter a word to be tested:\n")
palindrome_check = palindrome[-1::-1]
if(palindrome == palindrome_check):
    print("\'"+ palindrome +"\' is a palindrome.")
else:
    print("\'"+ palindrome +"\' is not a palindrome.")