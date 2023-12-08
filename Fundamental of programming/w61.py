## Take input for the list the split using the delimitor ,

def input_integers():
    input_string = input("Give integers separated by comma:\n")
    input_char = input_string.split(",")
    list_int=[]
    for ch in input_char:
        list_int.append(int(ch))
    return list_int

def remove_shit(nums: list):
    new_list = []
    ## iterate in the list to find the elements
    for num in nums:
        ## Add elements to the new list if they are not present
        if num not in new_list:
            new_list.append(num)

    return new_list


num = input_integers()
ans = remove_shit(num)
print("Original List:",num)
print("List with duplicates removed:",ans)
