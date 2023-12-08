def anagram(A,B):
    if(len(A) != len(B)):
        print(A,"and",B,"are not anagrams")
        return 0 
    cond = True
    for ch in A:
        
        for c in B:
            if(c == ch):
                cond = True
                break
            else:
                cond = False
        
        if(cond == False):
            print(A,"and",B,"are not anagrams")
            return 0

    print(A,"and",B,"are anagrams")

A = input("Enter string A:\n")
B = input("Enter string B:\n")
anagram(A,B)