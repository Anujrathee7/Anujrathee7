def input_integer():
    input_integer = input("Give integers separated by comma:\n")
    input_char = input_integer.split(",")
    
    int_list = []
     
    for ch in input_char:
        int_list.append(int(ch))
    
    return int_list

def reverse_sort(num: list):
    ans = []
    n = len(num)
    for i in num:
        ans.append(int(num[n-1]))
        n=n-1
    return ans

num = input_integer()
print("Reversed list:",reverse_sort(num))
            


